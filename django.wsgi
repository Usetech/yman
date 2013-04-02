<uwsgi>
    <socket>127.0.0.1:15081</socket>
    <master/>
    <processes>4</processes>
    <enable-threads/>

    <pythonpath>/home/yman/</pythonpath>
    <module>wsgi</module>

    <virtualenv>/home/envs/yman</virtualenv>

    <logto>/var/logs/yman_uwsgi_error.log</logto>
    <uid>www-data</uid>
    <gid>www-data</gid>
    <pidfile>/home/yman/uwsgi.pid</pidfile>
</uwsgi>