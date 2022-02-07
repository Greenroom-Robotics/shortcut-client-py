# After installing the swagger codegen tool...

java -jar swagger-codegen-cli.jar generate \
  -i https://shortcut.com/api/rest/v3/shortcut.swagger.json \
  -l python \
  -DpackageName=shortcut_client_py 
