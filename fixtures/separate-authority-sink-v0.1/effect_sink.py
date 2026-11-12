"""Separate SQLite sink; its fencing watermark is NOT automatically authoritative."""
import sqlite3

class EffectSink:
    def __init__(self):
        self.db = sqlite3.connect(':memory:', isolation_level=None)
        self.db.execute('CREATE TABLE fence(epoch INTEGER NOT NULL)')
        self.db.execute('INSERT INTO fence VALUES (1)')
        self.db.execute('CREATE TABLE effects(request TEXT PRIMARY KEY, epoch INTEGER NOT NULL)')

    def observe_epoch(self, epoch):
        self.db.execute('UPDATE fence SET epoch=MAX(epoch,?)', (epoch,))

    def commit(self, request, token, fenced):
        self.db.execute('BEGIN IMMEDIATE')
        try:
            watermark = self.db.execute('SELECT epoch FROM fence').fetchone()[0]
            if fenced and token < watermark:
                self.db.rollback()
                return 'DENY_FENCED'
            self.db.execute('INSERT INTO effects VALUES (?,?)', (request, token))
            self.db.commit()
            return 'ALLOW'
        except BaseException:
            self.db.rollback()
            raise

    def rows(self):
        return self.db.execute('SELECT request,epoch FROM effects ORDER BY request').fetchall()
