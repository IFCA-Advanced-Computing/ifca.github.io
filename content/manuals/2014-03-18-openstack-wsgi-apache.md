Title: Running OpenStack Havana services on mod_wsgi
Date: 2014-03-18 16:00
Category: manuals
Tags: cloud, OpenStack
Summary: This is a short manual explaining how to run the OpenStack services (Nova, Cinder, Keystone, Glance and Ceilometer) behind an Apache HTTP server using mod_wsgi.

It's been a while since we started deploying our OpenStack services behind
an [Apache HTTPD server](http://httpd.apache.org/), using `mod_wsgi`. We started
with Keystone, since it was something needed in order to get our
[VOMS Authentication Plugin](https://ifca.github.io/keystone-voms/) working, but
afterwards we decided to homogenize our setup and move all the services from
Eventlet to Apache.

All the OpenStack services are WSGI applications, and therefore they can be moved
easily from Eventlet to Apache running in prefork mode. Adam Young (one of the
Keystone core developers) wrote almost two years ago a great article about this:
"[Keystone should move to Apache HTTPD](http://adam.younglogic.com/2012/03/keystone-should-move-to-apache-httpd/)".
As you can infer from that article, there are several advantages that overcome de
configuration overhead of this setup. Namely we switched from Eventlet to Apache because
of the following reasons:

 - You can use any of the [authentication](http://httpd.apache.org/docs/2.2/howto/auth.html)
 modules that are available for Apache and configure Keystone to use
 [external authentication](http://docs.openstack.org/developer/keystone/external-auth.html).
 We are using this for several modules, but the most important for us is the
 [VOMS Authentication Plugin](https://ifca.github.io/keystone-voms/).
 - SSL configuration is handled by Apache and not by the OpenStack service itself. Since we
 are using [Puppet](http://puppetlabs.com/)  in our deployments we only need to create a
 template and apply it to all of our services, instead of configuring each of the services
 individually.

## Nova configuration
## Keystone configuration
## Glance configuration
## Cinder configuration
## Ceilometer configuration
