<p>
  In the next lecture, we'll install Cassandra into your sandbox. It's a
  complicated process, and a lot can go wrong. Really, if you're not pretty
  comfortable with Linux, you might want to just watch the exercises that
  involve Cassandra instead of running them yourself.
</p>
<p>
  One common issue is ending up in a state where your RPM database (which keeps
  track of what packages you have installed on your system) becomes corrupt.
  You'll experience this as seeing an error message like this:
</p>
<p>
  <code
    >rpmts_HdrFromFdno – error: rpmdbNextIterator – Header V3 RSA/SHA1
    Signature, key ID BAD</code
  >
</p>
<p>
  If you encounter this, "yum"&nbsp;will no longer work at all. But, there is a
  way to fix it.
</p>
<p>
  Just enter the following commands (you can paste them into PuTTY by
  right-clicking in the PuTTY terminal window after copying them; and be sure
  you've already run "<code>su root</code>" to run the following as the root
  user:)
</p>
<pre class="prettyprint linenums">
cd ~

wget http://mirror.centos.org/centos/6/os/x86_64/Packages/nss-softokn-freebl-3.14.3-23.3.el6_8.x86_64.rpm

rpm2cpio http://mirror.centos.org/centos/6/os/x86_64/Packages/nss-softokn-freebl-3.14.3-23.3.el6_8.x86_64.rpm | cpio -idmv

cp ./lib64/libfreeblpriv3.* /lib64</pre
>
<p>
  Now, yum should work again. Note that if you do a big "yum update" and the ssl
  library is updated, you may lose your connection via PuTTY. If you're
  disconnected, wait a couple of minutes to allow yum to finish what it's doing,
  issue an ACPI Shutdown command to the virtual machine (via the Machine
  menu,)&nbsp;restart the sandbox, and connect again.
</p>
<p>
  And if *that* didn't work, you can try following the similar instructions at
  <a
    href="https://techjourney.net/centos-yum-rpm-error-rpmts_hdrfromfdno-rpmdbnextiterator-header-v3-rsasha1-signature-key-id-bad/"
    rel="noopener noreferrer"
    target="_blank"
    >https://techjourney.net/centos-yum-rpm-error-rpmts_hdrfromfdno-rpmdbnextiterator-header-v3-rsasha1-signature-key-id-bad/</a
  >
  instead (follow the steps for x64 CentOS.)
</p>
