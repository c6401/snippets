xonsh
xontrib load vox 
$name = 'myapp'

cd /tmp/
rm -rf /tmp/$name
django-admin startproject $name
cd $name
git init
git add .
git commit -m 'Initial commit'

python3 -mvenv venv
vox activate ./venv
echo django >> ./requirements.txt
echo ipython >> ./requirements.txt
echo ipdb >> ./requirements.txt
pip install -r ./requirements.txt

./manage.py startapp main
git add main
./manage.py migrate
./manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('admin', 'admin@localhost', 'admin')
exit()

bash
git apply << EOF
--- a/main/views.py
+++ b/main/views.py
@@ -1,3 +1,6 @@
+from django.http import HttpResponse
 from django.shortcuts import render
 
-# Create your views here.
+
+def ping(request):
+    return HttpResponse('pong')
diff --git a/myapp/urls.py b/myapp/urls.py
index 16a6070..ca90b09 100644
--- a/myapp/urls.py
+++ b/myapp/urls.py
@@ -16,6 +16,9 @@ Including another URLconf
 from django.contrib import admin
 from django.urls import path
 
+from main.views import ping
+
 urlpatterns = [
     path('admin/', admin.site.urls),
+    path('ping/', ping),
 ]
EOF
exit

code .

### run
cd /tmp/$name
vox activate ./venv

./manage.py runserver
./manage.py runserver &

xdg-open http://127.0.0.1:8000/admin/
curl http://127.0.0.1:8000/ping/

sqlitebrowser ./db.sqlite3 &

cd ..
rm -rf ./myapp
exit
