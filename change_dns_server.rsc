:local defaultDNS "192.168.29.2"
:local fallbackDNS "1.1.1.1"

:global sendTelegramMessage do={
    :local message [:tostr $1]
    :local botToken "bot5561402281:AAHpIpMbgFJDj6QVYg8Z7lG3i6FCr3Nfm7o"
    :local chatID "508844726"
    :local urlApi "https://api.telegram.org/"
    :local url ($urlApi . $botToken . "/sendMessage?chat_id=" . $chatID . "&text=<code>" . $message . "</code>&parse_mode=HTML")
    :log info $url
    /tool fetch mode=https url=$url dst-path="/dev/null"
}

:if ([/ping $defaultDNS count=5 ] < 4) do={
  :if ([/ip dns get servers] = $defaultDNS) do={
      /ip dns set servers=$fallbackDNS
      /ip dhcp-server network set dns-server=$fallbackDNS numbers=0
      /ip dns set use-doh-server=https://cloudflare-dns.com/dns-query verify-doh-cert=no
      :log warning ("DNS Save: " . $fallbackDNS)
      $sendTelegramMessage ("DNS Save: " . $fallbackDNS)
  }
} else={
  :if ([/ip dns get servers] = $fallbackDNS) do={
      /ip dns set servers=$defaultDNS
      /ip dhcp-server network set dns-server=$defaultDNS numbers=0
      /ip dns set use-doh-server="" verify-doh-cert=no
      :log warning ("DNS Main: " . $defaultDNS)
      $sendTelegramMessage ("DNS Main: " . $defaultDNS)
  }
}

# Test script on console
# /system script run change_dns_serve

# Test bkp part
# /ip dns set servers=1.1.1.1; /ip dhcp-server network set dns-server=1.1.1.1 numbers=0

# Test ping on log
# :if ([/ping 192.168.29.2 count=1 as-value ] = 0) do={ :log info ("| CONTAMOS MAIS 1 | "); }
