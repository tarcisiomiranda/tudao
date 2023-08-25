:local failedCount 0
:local defaultDNS "192.168.29.2"
:local fallbackDNS "1.1.1.1"
:local currentDNS [/ip dns get servers]

:global sendTelegramMessage do={
    :local message [:tostr $1]
    :local botToken ""
    :local chatID ""
    :local url ("https://api.telegram.org/" . $botToken . "/sendMessage?chat_id=" . $chatID . "&text=" . $message)
    :log info $url
    /tool fetch mode=https url=$url dst-path="/dev/null"
}

:if ([/ping $defaultDNS count=1] = 0) do={
    :set failedCount ($failedCount + 1)
    :if ($failedCount = 5) do={
        :if ($currentDNS = $defaultDNS) do={
            /ip dns set servers=$fallbackDNS
            /ip dhcp-server network set dns-server=$fallbackDNS numbers=0
            /ip dns set use-doh-server=https://cloudflare-dns.com/dns-query verify-doh-cert=yes
            :log warning ("DNS Backup apply, " . $fallbackDNS . " due to ping failure.")
            $sendTelegramMessage ("DNS Backup apply " . $fallbackDNS . " due to ping failure.")
        }
    }
} else={
    :set failedCount 0
    :if ($currentDNS = $fallbackDNS) do={
        /ip dns set servers=$defaultDNS
        /ip dhcp-server network set dns-server=$defaultDNS numbers=0
        /ip dns set use-doh-server="" verify-doh-cert=no
        :log warning ("DNS Main apply, " . $defaultDNS . " after successful ping.")
        $sendTelegramMessage ("DNS Main apply " . $defaultDNS . " after successful ping.")
    }
}

:log info ("Actual value failedCount: " . $failedCount)
