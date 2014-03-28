Title: POSTPONED: SL5 User Interfaces deprecation plan (2)
Data: 2014-03-31 09:00
Category: news
Tags: grid, user interface, Scientific Linux 5
Author: aloga
Slug: sl5-user-interfaces-deprecation-plan2
Summary: NEW Dates for the Scientific Linux 5-based user interfaces (UIs) deprecation plan.


Due to a mistake with the dates, the deprecation plan has been **POSTPONED** until April 7th 2014.
Please check the new plan below.

---

After the postponed
[SLC5 deprecation plan](|filename|/news/2013-11-25-slc5-deprecation.md)
we have restablish the procedure to deprecate the Scientific Linux 5 user interfaces.
The operating system on these machines has become obsolete and are going to be removed
according to the following deprecation plan.

## Deprecation plan

1. April 7th 2014: `gridui.ifca.es` will stop pointing to the Scientific
   Linux 5 machines, and will redirect users to the Scientific Linux 6
   machines.
1. April 14th 2014: `griduisl5.ifca.es` will become unavailable, therefore
   there will be no access to the Scientific Linux 5 machines anymore. Please,
   update your working environment before that date.
1. April 30th 2014: Deletion and removal of machines.

## SSH warnings about host identification changed

Please take into account that on April 7th the fingerprint of `gridui.ifca.es` will
change. It is possible that you will get messages like this:

    :::shell-session
    user@mymachine:~ $ ssh user@gridui.ifca.es
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
    Someone could be eavesdropping on you right now (man-in-the-middle attack)!
    It is also possible that a host key has just been changed.
    The fingerprint for the RSA key sent by the remote host is
    29:80:9b:28:e7:8a:00:fe:6c:60:ef:e6:a6:71:33:bd.
    Please contact your system administrator.
    Add correct host key in /home/user/.ssh/known_hosts to get rid of this message.
    Offending RSA key in /home/user/.ssh/known_hosts:58
      remove with: ssh-keygen -f "/home/user/.ssh/known_hosts" -R gridui.ifca.es
    RSA host key for gridui has changed and you have requested strict checking.
    Host key verification failed.

Check that the new fingerprint is **exactly** `29:80:9b:28:e7:8a:00:fe:6c:60:ef:e6:a6:71:33:bd`. If it is, then
you can safely remove the offending match with the following command:

    :::shell-session
    user@mymachine:~ $ ssh-keygen -f "/home/user/.ssh/known_hosts" -R gridui.ifca.es
    # Host griduisl6 found: line 58 type RSA
    /home/user/.ssh/known_hosts updated.
    Original contents retained as /home/user/.ssh/known_hosts.old

## Access to legacy SL5 machines

Access to Scientific Linux 5 machines is still provided trough the
[batch system](https://grid.ifca.es/wiki/Cluster/Usage#Access_to_Scientific_Linux_5_machines).
In order to request a Scientific Linux 5 machine you must specify the complex `scientificlinux5` like this:

    :::shell-session
    user@cloudprv-10-0:~ $ qsub -l scientificlinux5=true (...)

If you want an interactive session, request one with `qlogin`:

    :::shell-session
    user@cloudprv-10-0:~ $ qlogin -l scientificlinux5=true (...)
    JSV "/nfs4/opt/gridengine/util/resources/jsv/jsv-IFCA.tcl" has been started
    JSV "/nfs4/opt/gridengine/util/resources/jsv/jsv-IFCA.tcl" has been stopped
    Your job 1822278 ("QLOGIN") has been submitted
    waiting for interactive job to be scheduled ...
    Your interactive job 1822278 has been successfully scheduled.
    Establishing builtin session to host cloudprv-02-9.ifca.es ...
    user@cloudprv-02-9:~$ cat /etc/redhat-release
    Scientific Linux SL release 5.5 (Boron)
    user@cloudprv-02-9:~$


## Support

If there is any user, group or software administrator that cannot reach the
described deadline, please open a ticket on [our support helpdesk](https://support.ifca.es/)
as soon as possible, explaining your situation.
