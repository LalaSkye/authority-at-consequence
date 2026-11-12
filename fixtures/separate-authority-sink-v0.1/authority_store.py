"""Synthetic authoritative epoch in a dedicated SQLite connection."""
import sqlite3

class AuthorityStore:
    def __init__(self):
        self.db = sqlite3.connect(':memory:', isolation_level=None)
        self.db.execute('CREATE TABLE authority(epoch INTEGER NOT NULL, allowed INTEGER NOT NULL)')
        self.db.execute('INSERT INTO authority VALUES (1,1)')

    def approval(self):
        epoch, allowed = self.db.execute('SELECT epoch,allowed FROM authority').fetchone()
        assert allowed
        return epoch

    def revoke(self):
        self.db.execute('UPDATE authority SET epoch=epoch+1, allowed=0')

    def snapshot(self):
        return self.db.execute('SELECT epoch,allowed FROM authority').fetchone()
