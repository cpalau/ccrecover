var _____WB$wombat$assign$function_____=function(name){return (globalThis._wb_wombat && globalThis._wb_wombat.local_init && globalThis._wb_wombat.local_init(name))||globalThis[name];};if(!globalThis.__WB_pmw){globalThis.__WB_pmw=function(obj){this.__WB_source=obj;return this;}}{
let window = _____WB$wombat$assign$function_____("window");
let self = _____WB$wombat$assign$function_____("self");
let document = _____WB$wombat$assign$function_____("document");
let location = _____WB$wombat$assign$function_____("location");
let top = _____WB$wombat$assign$function_____("top");
let parent = _____WB$wombat$assign$function_____("parent");
let frames = _____WB$wombat$assign$function_____("frames");
let opener = _____WB$wombat$assign$function_____("opener");
function externalLinks() {
    if (!document.getElementsByTagName) return;
    var anchors = document.getElementsByTagName("a");
    for (var i=0; i<anchors.length; i++) 
    {
        var anchor = anchors[i];
        if (anchor.getAttribute("href") &&
        anchor.getAttribute("rel") == "external")
        anchor.target = "_blank";
    }
}
window.onload = externalLinks;

}

/*
     FILE ARCHIVED ON 23:53:02 Dec 09, 2013 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 17:47:28 Nov 06, 2026.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 0.384
  exclusion.robots: 0.04
  exclusion.robots.policy: 0.031
  esindex: 0.007
  cdx.remote: 7.084
  LoadShardBlock: 120.813 (3)
  PetaboxLoader3.datanode: 143.4 (4)
  load_resource: 148.348
  PetaboxLoader3.resolve: 71.561
*/