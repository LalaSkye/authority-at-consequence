import unittest
from receiver import Scenario

class SeparateStoreCases(unittest.TestCase):
    def test_s1_unfenced_forbidden_effect(self):
        x=Scenario(); token=x.approval(); x.revoke()
        decision, committed, violation=x.effect(token, fenced=False)
        self.assertEqual((decision,committed,violation), ('ALLOW',True,True))
        self.assertEqual(len(x.sink.rows()),1)
        self.assertEqual([event for event,_ in x.trace],['approval','revocation','effect'])

    def test_s2_fenced_sink_observed(self):
        x=Scenario(); token=x.approval(); x.revoke(); x.notify_sink()
        self.assertEqual(x.effect(token, fenced=True),('DENY_FENCED',False,False))
        self.assertEqual(x.sink.rows(),[])
        self.assertEqual([event for event,_ in x.trace],['approval','revocation','sink_observed','effect'])

    def test_s3_fenced_sink_unaware(self):
        x=Scenario(); token=x.approval(); x.revoke()
        self.assertEqual(x.effect(token, fenced=True),('ALLOW',True,True))
        self.assertEqual(x.sink.rows(),[('doc-001',1)])
        self.assertEqual([event for event,_ in x.trace],['approval','revocation','effect'])

    def test_s4_effect_precedes_revocation(self):
        x=Scenario(); token=x.approval()
        self.assertEqual(x.effect(token, fenced=True),('ALLOW',True,False))
        x.revoke()
        self.assertEqual(x.sink.rows(),[('doc-001',1)])
        self.assertEqual([event for event,_ in x.trace],['approval','effect','revocation'])

if __name__ == '__main__': unittest.main()
