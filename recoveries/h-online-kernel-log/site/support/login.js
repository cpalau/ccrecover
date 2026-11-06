var _____WB$wombat$assign$function_____=function(name){return (globalThis._wb_wombat && globalThis._wb_wombat.local_init && globalThis._wb_wombat.local_init(name))||globalThis[name];};if(!globalThis.__WB_pmw){globalThis.__WB_pmw=function(obj){this.__WB_source=obj;return this;}}{
let window = _____WB$wombat$assign$function_____("window");
let self = _____WB$wombat$assign$function_____("self");
let document = _____WB$wombat$assign$function_____("document");
let location = _____WB$wombat$assign$function_____("location");
let top = _____WB$wombat$assign$function_____("top");
let parent = _____WB$wombat$assign$function_____("parent");
let frames = _____WB$wombat$assign$function_____("frames");
let opener = _____WB$wombat$assign$function_____("opener");
/* login.js
 * (c) 2006 Heise Zeitschriften Verlag
 * $Id: login.js,v 1.3 2006/11/06 15:06:24 sn Exp $
 */

function __heise_loginout () {
	var sslprefix = '';
	if (location.hostname == "www.heise-online.co.uk") {
		sslprefix = 'http://' + location.hostname;
	}

	var sso_base = sslprefix + '/userdb/sso?dirid=1';
	var reg_base = sslprefix + '/userdb/register?dirid=1';
	var fw		 = '&amp;forward=' + escape(location.href);
	var sso_in	 = sso_base + '&amp;rm=show_login' + fw;
	var sso_out	 = sso_base + '&amp;rm=do_logout'  + fw;
	var sso_reg	 = reg_base + '&amp;rm=show_registration';
	var sso_data     = reg_base + '&amp;rm=show_userdata' + fw;
	return((document.cookie.indexOf("ssologin=") == -1)
		? 'You are a guest <span class="dot">&#8226;</span> <a href="'+sso_in+'">Login</a> | <a href="'+sso_reg+'">Register</a>'
		: '<span class="logged">You are logged in</span> <span class="dot">&#8226;</span> <a href="'+sso_out+'">Logout</a> | <a href="'+sso_data+'">Profile</a>');
}
document.write("<div id=\"login\">" + __heise_loginout() + "</div>");

}

/*
     FILE ARCHIVED ON 14:56:28 Jun 18, 2009 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 17:48:11 Nov 06, 2026.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 0.697
  exclusion.robots: 0.06
  exclusion.robots.policy: 0.046
  esindex: 0.008
  cdx.remote: 7.084
  LoadShardBlock: 290.431 (6)
  PetaboxLoader3.datanode: 241.286 (7)
  PetaboxLoader3.resolve: 92.178 (4)
  load_resource: 146.656
*/