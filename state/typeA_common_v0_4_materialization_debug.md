# Type-A common v0.4 materialization debug

- run commit: 138a9bcfcbb6f059c978c38a1bc185b595b241fd
- exit code: 1

```text
Traceback (most recent call last):
  File "/home/runner/work/fame_outcome_followup/fame_outcome_followup/scripts/build_typeA_common_master_v0_4.py", line 201, in <module>
    if __name__=='__main__': main()
                             ^^^^^^
  File "/home/runner/work/fame_outcome_followup/fame_outcome_followup/scripts/build_typeA_common_master_v0_4.py", line 87, in main
    assert len(rr)==1 and rr[0]['cohort_unit']=='khan_2005_korea_leaders60_politics10'
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```
