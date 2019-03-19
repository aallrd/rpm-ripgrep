# rpm-internal-ripgrep

Build a RPM package for the **internal-ripgrep** project.

## RPM build

```
$ docker run --rm -it --volume $(pwd):/specs --volume $(pwd):/output localhost:5000/aallrd/internal-build-rpm --build
[INFO] [14:32:47] RPM spec file: ripgrep.spec
[...]
[SUCCESS] [10:37:40] Binary RPM file(s):
[SUCCESS] [10:37:40] * /root/rpmbuild/RPMS/x86_64/internal-ripgrep-0.10.0-1.el6.x86_64.rpm
[SUCCESS] [10:37:40] Source RPM file(s):
[SUCCESS] [10:37:40] * /root/rpmbuild/SRPMS/internal-ripgrep-0.10.0-1.el6.src.rpm
```

## RPM installation

### Using YUM

```
# Configure the vendor repo on the server
$ cat <<EOF >> /etc/yum.repos.d/vendors.repo

[vendor-internal]
name=internal
baseurl=http://localhost:4000/vendors/internal
enabled=1
gpgcheck=0
proxy=_none_
EOF

# Install the package using Yum
$ yum install -y --disablerepo=* --enablerepo=internal internal-ripgrep
```

### Using RPM

```
$ wget http://localhost:4000/vendors/internal/internal-ripgrep-0.10.0-1.el6.x86_64.rpm
$ rpm -ivh internal-ripgrep-0.10.0-1.el6.x86_64.rpm
Preparing...        ########################################### [100%]
   1:internal-ripgrep  ########################################### [100%]
```

## Usage

```
$ rg --version
ripgrep 0.10.0 (rev 8a7db1a918)
-SIMD -AVX (compiled)
+SIMD -AVX (runtime)
```

