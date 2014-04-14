%define	module	pybox2d
Name:           python-%{module}
Version:        2.0.2b2
Release:        1
Summary:        A 2D rigid body simulation library for Python

Group:          Development/Python
License:        zlib
URL:            http://code.google.com/p/pybox2d/
Source0:        http://pybox2d.googlecode.com/files/%{module}-%{version}.zip

BuildRequires:  gcc
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  swig
Provides:	%{module} = %{version}-%{release}
Obsoletes:	%{module} < 2.0.2b2-3

%description
Programmer's can use Box2D in their games to make objects move in
believable ways and make the world seem more interactive. From the
game's point of view a physics engine is just a system for procedural
animation. Rather than paying (or begging) an animator to move your
actors around, you can let Sir Isaac Newton do the directing.


%prep
%setup -q -n Box2D-%{version}

# calm rpmlint down
sed -i LICENSE README -e 's/\r//'
chmod go-w -R *
 

%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# copy missing files
cp Box2D.py %{buildroot}%{python_sitearch}/Box2D/

%files
%doc LICENSE README doc/*
%{python_sitearch}/*



