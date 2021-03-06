#!/usr/bin/python
#-*- coding: utf-8 -*-
require_once("./includes/general.php")
header("Content-Type: text/plain")
header("Content-Encoding: UTF-8")
header("Expires: Mon, 26 Jul 1997 05:00:00 GMT")
header("Last-Modified: "+gmdate("D, d M Y H:i:s")+" GMT")
header("Cache-Control: no-store, no-cache, must-revalidate")
header("Cache-Control: post-check=0, pre-check=0", False)
header("Pragma: no-cache")
raw = ""
if isset(_POST["json_data"]):
  raw = getRequestParam("json_data")
if !raw&&isset(_GLOBALS)&&isset(_GLOBALS["HTTP_RAW_POST_DATA"]):
  raw = _GLOBALS["HTTP_RAW_POST_DATA"]
if !raw&&isset(HTTP_RAW_POST_DATA):
  raw = HTTP_RAW_POST_DATA
if !raw:
  if !function_exists("file_get_contents"):
    fp = fopen("php://input", "r")
    if fp:
      raw = ""
      while :
        raw = fread(fp, 1024)
      fclose(fp)
  else:
    raw = ""+file_get_contents("php://input")
if !raw:
  die("{"result":null,"id":null,"error":{"errstr":"Could not get raw post data.","errfile":"","errline":null,"errcontext":"","level":"FATAL"}}")
if isset(config["general.remote_rpc_url"]):
  url = parse_url(config["general.remote_rpc_url"])
  req = "POST "+url["path"]+" HTTP/1.0\n"
  req+="Connection: close\n"
  req+="Host: "+url["host"]+"\n"
  req+="Content-Length: "+strlen(raw)+"\n"
  req+="\n"+raw
  if !isset(url["port"])||!url["port"]:
    url["port"] = 80
  errno = errstr = ""
  socket = fsockopen(url["host"], intval(url["port"]), errno, errstr, 30)
  if socket:
    fputs(socket, req)
    resp = ""
    while :
      resp+=fgets(socket, 4096)
    fclose(socket)
    resp = explode("\n\n", resp)
    print(resp[1])
  die(0)
json = Moxiecode_JSON()
input = json.decode(raw)
if isset(config["general.engine"]):
  spellchecker = config["general.engine"](config)
  result = call_user_func_array([spellchecker, input["method"]], input["params"])
else:
  die("{"result":null,"id":null,"error":{"errstr":"You must choose an spellchecker engine in the config.php file.","errfile":"","errline":null,"errcontext":"","level":"FATAL"}}")
output = {"id":input.id, "result":result, "error":}
print(json.encode(output))
