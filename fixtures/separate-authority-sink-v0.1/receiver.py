"""Deterministic event trace and independent safety oracle."""
from authority_store import AuthorityStore
from effect_sink import EffectSink

class Scenario:
    def __init__(self):
        self.authority = AuthorityStore()
        self.sink = EffectSink()
        self.trace = []

    def approval(self):
        epoch = self.authority.approval()
        self.trace.append(('approval', epoch))
        return epoch

    def revoke(self):
        self.authority.revoke()
        self.trace.append(('revocation', self.authority.snapshot()[0]))

    def notify_sink(self):
        epoch = self.authority.snapshot()[0]
        self.sink.observe_epoch(epoch)
        self.trace.append(('sink_observed', epoch))

    def effect(self, token, fenced, request='doc-001'):
        before = self.authority.snapshot()
        decision = self.sink.commit(request, token, fenced)
        rows = self.sink.rows()
        committed = (request, token) in rows
        violation = committed and (not before[1] or token != before[0])
        self.trace.append(('effect', {'authority_epoch':before[0], 'authority_allowed':before[1], 'token':token, 'fenced':fenced, 'decision':decision, 'sink_rows':rows, 'safety_violation':violation}))
        return decision, committed, violation
