#!/usr/bin/python3
import os, sys

class color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'

print(color.BOLD + color.GREEN + "Spotify Adblocker\nSimple script based on a Reddit thread for google ads and spotify ads links.\n" + color.YELLOW + "mrtunne.info")
if sys.platform == "win32":
    import ctypes
    if ctypes.windll.shell32.IsUserAnAdmin() == 1:
        with open(os.environ['WINDIR'] + '\\System32\\drivers\\etc\\hosts', 'a') as f:
            f.write('0.0.0.0 adclick.g.doublecklick.net\n0.0.0.0 adeventtracker.spotify.com\n0.0.0.0 ads-fa.spotify.com\n0.0.0.0 analytics.spotify.com\n0.0.0.0 audio2.spotify.com\n0.0.0.0 b.scorecardresearch.com\n0.0.0.0 bounceexchange.com\n0.0.0.0 bs.serving-sys.com\n0.0.0.0 content.bitsontherun.com\n0.0.0.0 core.insightexpressai.com\n0.0.0.0 crashdump.spotify.com\n0.0.0.0 d2gi7ultltnc2u.cloudfront.net\n0.0.0.0 d3rt1990lpmkn.cloudfront.net\n0.0.0.0 desktop.spotify.com\n0.0.0.0 doubleclick.net\n0.0.0.0 ds.serving-sys.com\n0.0.0.0 googleadservices.com\n0.0.0.0 googleads.g.doubleclick.net\n0.0.0.0 gtssl2-ocsp.geotrust.com\n0.0.0.0 js.moatads.com\n0.0.0.0 log.spotify.com\n0.0.0.0 media-match.com\n0.0.0.0 omaze.com\n0.0.0.0 open.spotify.com\n0.0.0.0 pagead46.l.doubleclick.net\n0.0.0.0 pagead2.googlesyndication.com\n0.0.0.0 partner.googleadservices.com\n0.0.0.0 pubads.g.doubleclick.net\n0.0.0.0 redirector.gvt1.com\n0.0.0.0 s0.2mdn.net\n0.0.0.0 securepubads.g.doubleclick.net\n0.0.0.0 spclient.wg.spotify.com\n0.0.0.0 tpc.googlesyndication.com\n0.0.0.0 v.jwpcdn.com\n0.0.0.0 video-ad-stats.googlesyndication.com\n0.0.0.0 weblb-wg.gslb.spotify.com\n0.0.0.0 www.googleadservices.com\n0.0.0.0 www.googletagservices.com\n0.0.0.0 www.omaze.com')
            print(color.YELLOW + "===================================\n" + color.RED + "Done." + color.YELLOW + "\n===================================")
    else:
        print(color.RED + 'You need Administrator permissions to do this. Try opening your CMD/PowerShell with' + color.GREEN + "Open As Administrator")
        sys.exit(1)
elif sys.platform == "linux":
    if os.geteuid() == 0:
        with open('/etc/hosts', 'a') as f:
            f.write('0.0.0.0 adclick.g.doublecklick.net\n0.0.0.0 adeventtracker.spotify.com\n0.0.0.0 ads-fa.spotify.com\n0.0.0.0 analytics.spotify.com\n0.0.0.0 audio2.spotify.com\n0.0.0.0 b.scorecardresearch.com\n0.0.0.0 bounceexchange.com\n0.0.0.0 bs.serving-sys.com\n0.0.0.0 content.bitsontherun.com\n0.0.0.0 core.insightexpressai.com\n0.0.0.0 crashdump.spotify.com\n0.0.0.0 d2gi7ultltnc2u.cloudfront.net\n0.0.0.0 d3rt1990lpmkn.cloudfront.net\n0.0.0.0 desktop.spotify.com\n0.0.0.0 doubleclick.net\n0.0.0.0 ds.serving-sys.com\n0.0.0.0 googleadservices.com\n0.0.0.0 googleads.g.doubleclick.net\n0.0.0.0 gtssl2-ocsp.geotrust.com\n0.0.0.0 js.moatads.com\n0.0.0.0 log.spotify.com\n0.0.0.0 media-match.com\n0.0.0.0 omaze.com\n0.0.0.0 open.spotify.com\n0.0.0.0 pagead46.l.doubleclick.net\n0.0.0.0 pagead2.googlesyndication.com\n0.0.0.0 partner.googleadservices.com\n0.0.0.0 pubads.g.doubleclick.net\n0.0.0.0 redirector.gvt1.com\n0.0.0.0 s0.2mdn.net\n0.0.0.0 securepubads.g.doubleclick.net\n0.0.0.0 spclient.wg.spotify.com\n0.0.0.0 tpc.googlesyndication.com\n0.0.0.0 v.jwpcdn.com\n0.0.0.0 video-ad-stats.googlesyndication.com\n0.0.0.0 weblb-wg.gslb.spotify.com\n0.0.0.0 www.googleadservices.com\n0.0.0.0 www.googletagservices.com\n0.0.0.0 www.omaze.com')
            print(color.YELLOW + "===================================\n" + color.RED + "Done." + color.YELLOW + "\n===================================")
    else:
            print(color.RED + 'You need ROOT permissions to do this. Try opening this file with ' + color.GREEN + "sudo")
            sys.exit(1)
else:
    print(color.RED + "Unsupported operating system.")
