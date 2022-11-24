import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.pexels.com/videos/")

soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())


'''

<!DOCTYPE html>
<html lang="en-US">
 <head>
  <title>
   Just a moment...
  </title>
  <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
  <meta content="IE=Edge" http-equiv="X-UA-Compatible"/>
  <meta content="noindex,nofollow" name="robots"/>
  <meta content="width=device-width,initial-scale=1" name="viewport"/>
  <link href="/cdn-cgi/styles/challenges.css" rel="stylesheet"/>
 </head>
 <body class="no-js">
  <div class="main-wrapper" role="main">
   <div class="main-content">
    <h1 class="zone-name-title h1">
     <img class="heading-favicon" onerror="this.onerror=null;this.parentNode.removeChild(this)" src="/favicon.ico"/>
     www.pexels.com
    </h1>
    <h2 class="h2" id="challenge-running">
     Checking if the site connection is secure
    </h2>
    <noscript>
     <div id="challenge-error-title">
      <div class="h2">
       <span class="icon-wrapper">
        <div class="heading-icon warning-icon">
        </div>
       </span>
       <span id="challenge-error-text">
        Enable JavaScript and cookies to continue
       </span>
      </div>
     </div>
    </noscript>
    <div id="trk_jschal_js" style="display:none;background-image:url('/cdn-cgi/images/trace/managed/nojs/transparent.gif?ray=76f40405ac66f3c9')">
    </div>
    <div class="core-msg spacer" id="challenge-body-text">
     www.pexels.com needs to review the security of your connection before proceeding.
    </div>
    <form action="/videos/?__cf_chl_f_tk=272zXSN.a4e2I1O7dmqsqjauBvHThfx5NiXYrUgBL68-1669312528-0-gaNycGzNB1E" enctype="application/x-www-form-urlencoded" id="challenge-form" method="POST">
     <input name="md" type="hidden" value="UzTzRGy6CbtjMgNbj2Nx3KZ4d0AfHJ0xLvaDtJ1EpLA-1669312528-0-AdwjXbQvnIwou64zmgbJQQJfsnyjClip_dRo21407k02A21zjRiHZyHJ429oDByoppGse8p4b8uWNHaNSpthZUu3ZreTljItr43Kdqabb_TaoWfvoKk4w9otaVrWwky_WUFwt1p0O5SxlAxAvxn0qqmMTOKAC3KgKkaEN5uhDjYZY7gSFLDunLd9zBNzbHHkn_N8Y5j4tXfyprbnEoEtyzyDAQxESAFrs57yuvLUIeSTjxrJnaURU4tNfpl6ZWLp42KAOx8si5SSxuqhnJHbZvbhzkrS4uSko4JLnCT5YcXqtcGtcMGRsKdSNkwDxjPJ5fgGckzcZvzVJpa180IlKaITTZzbuUtLAGSsm8ocsBINhOH8pGeBOp21ptWsaVkIDWe1x1co37mrCB5nOCDhCrNWg9PH17bmMi30ILcuPZvUURItUhouhuaEsatIfC1K8Z90RtZ6uUGThIsckxawWqNuPVgFBLVvL7Z7YAtNdYuvoMFcBWe7Vcmu9BtxePdYAcZ1nQaKOqE2rdQ_pgXcj5OcL1i0--Iq-KYU_1Y3KO3MiaVafV6DhLkE8st1HQtpCvErF_h4XRtQ_6tx4_KaZVBtJT1V_bkJaxHK4IQ2nnHrTiUl2NWvF1y6YcPa-zmd91VHVuDTgOcn9oQ_Q5t_JCo"/>
     <input name="r" type="hidden" value="DgeM5zAA9h03nwd4wjfJXXEUxb48J_.onsj.RnHdLNM-1669312528-0-AZdTJ6yuveJkhwBj7KOR5pxJxDFU3Tp3+Pp0kDEHx4KUNBkdGxvSTwQZnpmDieu4yvNCG/wZ1Ke5GBir2UK13gL5Cerc1A7qfTi9mKEMozSCdW0uemTUjYYNRY7puMRbmcgJzyED77nZL3IQ13mBLvpaLpUSr3xBy6DvMEIpY9nwQFx1nYCTu6ABBazVgFkyJ4DQDORIuf59mM+AcwBp2/cC9Y5Eb1u6Rxf2xLj1RIb2e07BCR8cXvBT59XWUCctus6CYwYV3y3RudCW/LsEKO0v2Z0SasjgwL7TRAlV+YGwIKQVcsKiSLHEVXnzWqtnpA5LH7ONR0k3dXESqkDhJ1a/IQcwcx7o/4Bb5JSmRs+suM0agt/JCRZY8AiRMUVaxR+pKQNt/+mbZDkGhRmF8j/ajwrGWj6st0GlV1GeQ4y/e/UpzaPu/Vk338rprbBT4zvALXffav6iLBHLCKlvxxqkteU1tgVtv3nQ2seVoh1F5c2/a0txeuPrTLdc/M86tUpJJRJnKPL5gmPJQY5AhVaaEuGKv+5S4H+PAd48dGiBUqURL9h64XYELhAr/8Fa9x80YB6FoqqN+OS0JUTRVyRkOdh0J7gL4bDXSKGDrBN4f7dRbyZjdl8EKuBnR2LhESgTPpe8RbtZkzDUSzhFKBx3v1L/KXETImqabp2i1XvYZvboVSuQgDSLnnkjhaZQK5NofgexZJ+jZL6qlIcFmFHv9m46GgJ1dZ9mYx/jwbSnRDu9updxPoaEkLeloz2sQUQ/J8+EmRc8Y5/JN+CODiWOHkg8Ck0jV/f135oXmR/pykk0SGXmmtXc4PFEfW7Jq3P3IVv2jPY7KLZxAEvqA6RfVE/dCosSYxJ8O/CiuYpB4/loOlXay6C1bqAdC3J+cx8imfYsj63MD+FH5VZ0cdqD2RmskHurtKC/avnKSwA/Juv2pcC86c5KcMh/r1MN1DYZ0ZiZo5n6KO74oUIGZDW7a2iCSageWU+Meqy4+O82hQ9Umuwch2DwLT9LUZY4E04wNZJ3/Z0wLb++MaEEhmqYw9NKW0SXYS98povgeUOxd3FDSUbU8kIPylaXeRN3XE0ZfqPyW6PTEJY+ejKI+EBTYjqBAhQwCz10HNbfHiwoxmceG8GKbhpSExxfVr+sPPjBx8D8l8G421y+3X4kMCTAPnoOywiybk5knjqv2z/3J+UjCLNCxTUL69SB0jKZzciXvNIfuN/Mqr3EZhdLQEJbUIIy+XCMYcNsRArFAEymCsxcZvdNNqaQcgyrTmq4yw/CjFaoJGuOyIpIx+KRW5uC9Ekrk3GFyH5Djr7vTdLRMYDYV+04lLhBhPGQqCEdwnVSSHi5fSZZIuT8GSgWXwgxZoPK8beAmu/g/LlA/qqu9yDWtjzZkJf4+BPSkxmCR5wr6z1BKg3440jRAsB5lTOMRKy+MSY7fMQMSnZi8grAX2B04qHANfwMFbNkyabZl1AjCEMeEQx2MzKLX01vOEDKVBFvPRk6dAR0VSzcDVlqHsNnI5qrsg0r/BjQkaoFrOP2WbGt2mkJNAlnXkhRBoLk3z58g7P7yRR30GLW9qcLA3rpXWviBE0o7NcaPpKVY+5o8t8Klb12f4ZiTFqBpAQd8zABQg09nzz0J1EqulfTTXcPB2xPTRxh4JPpcrGWC9KFvymyDQPNyNRvBHAWv9Mz0IN9xQGCX2ba15QnIItrP6ztkivKxyRVCvryp+iU5twb7x4TaEFWKodHqjExkPR9Y/10sDwuRduZreAtIxpxHdxqxY9upvvtEnoN3cJ1ny+4+z+j3jLHx7mdGmMiA34="/>
    </form>
   </div>
  </div>
  <script>
   (function(){
        window._cf_chl_opt={
            cvId: '2',
            cType: 'managed',
            cNounce: '82188',
            cRay: '76f40405ac66f3c9',
            cHash: '088a42b0f30458c',
            cUPMDTk: "\/videos\/?__cf_chl_tk=272zXSN.a4e2I1O7dmqsqjauBvHThfx5NiXYrUgBL68-1669312528-0-gaNycGzNB1E",
            cFPWv: 'b',
            cTTimeMs: '1000',
            cTplV: 4,
            cTplB: 'cf',
            cRq: {
                ru: 'aHR0cHM6Ly93d3cucGV4ZWxzLmNvbS92aWRlb3Mv',
                ra: 'cHl0aG9uLXJlcXVlc3RzLzIuMjUuMQ==',
                rm: 'R0VU',
                d: 'OW8nBynH6Rg6HGVsVkRS9YgicC7kvUkAd4neTkDp2QNm/HbqZyUDnUO5+StGenRCKWZ7hrbI35pPlQGQrDfJQVV9Vmxb40LfxC9Yp2bNIqO/+pGqlYtVlXL/AwW2NMwxcqvaZeSIfAB2kvdkyJWyUqZZuKNTYEzmm0lTTtZp0pbwd4l5zE5Tsn7AMEFWR2wS3wgAGCOJ32JQRNXPedv0g0sbVgjeEjTWIVmCO3MIO7TtRJuT9DsPJtYB7/EKYohwgnpIaDYOOB8WydXDPAn0fxGBuwz9oHiK+Nd7M1cuiOuhsL0CHcwXfnxyDWXQqJysInscYlwQLWK6p64x5OikmgQWbXizWZGX+uy5fjOZo+rAFxebRWQYSjO7ii//K/gFK4ZN0ZjLGyh9RmVygvGpU74s4I2jguYE/WKsStpgk66eMbrGedUwvuIYCktUkdLGS46BlzSN9pOFlHwVUz+sO3elOfTcPbNTAWXQgO8/ovnQIMe/dQpSgID5fzlwiKhZYye8xZ8AnahZtua+XVAWWIDuq7K3hsX7xt4MBdpAkVU62rik1vQXH/SKCD7yFnoN0aFQRmyarYNLPhpcz5B9iyguPfNde4tfV8qwIsa3K+T3MdfyE7HRhVmMXlY/vSkIwxN58lxjTmHU3Aw5xtWhFw==',
                t: 'MTY2OTMxMjUyOC4yNzEwMDA=',
                m: 'rbydHsw9aZCvmJK+Imwm6Ovs0EU5jAygYcAlfDktHQM=',
                i1: 'VJ0m4BAw5HI5P1IppWLs5Q==',
                i2: 'YBR6vf9N/Ujjdeiwb5Op1g==',
                zh: 'NNvtYPqUSp5OZQlBARs/elbgaYo5sB6TI6GfvNyxORY=',
                uh: '5GU+jYv2xJ+bCaE/ARmi/DORbiS/v56CW7E0TH4XWQk=',
                hh: 'Q3T1VSV1376IoXShdoD7ceOIGJMapzzf5okB22fCjaY=',
            }
        };
        var trkjs = document.createElement('img');
        trkjs.setAttribute('src', '/cdn-cgi/images/trace/managed/js/transparent.gif?ray=76f40405ac66f3c9');
        trkjs.setAttribute('style', 'display: none');
        document.body.appendChild(trkjs);
        var cpo = document.createElement('script');
        cpo.src = '/cdn-cgi/challenge-platform/h/b/orchestrate/managed/v1?ray=76f40405ac66f3c9';
        window._cf_chl_opt.cOgUHash = location.hash === '' && location.href.indexOf('#') !== -1 ? '#' : location.hash;
        window._cf_chl_opt.cOgUQuery = location.search === '' && location.href.slice(0, -window._cf_chl_opt.cOgUHash.length).indexOf('?') !== -1 ? '?' : location.search;
        if (window.history && window.history.replaceState) {
            var ogU = location.pathname + window._cf_chl_opt.cOgUQuery + window._cf_chl_opt.cOgUHash;
            history.replaceState(null, null, "\/videos\/?__cf_chl_rt_tk=272zXSN.a4e2I1O7dmqsqjauBvHThfx5NiXYrUgBL68-1669312528-0-gaNycGzNB1E" + window._cf_chl_opt.cOgUHash);
            cpo.onload = function() {
                history.replaceState(null, null, ogU);
            };
        }
        document.getElementsByTagName('head')[0].appendChild(cpo);
    }());
  </script>
  <div class="footer" role="contentinfo">
   <div class="footer-inner">
    <div class="clearfix diagnostic-wrapper">
     <div class="ray-id">
      Ray ID:
      <code>
       76f40405ac66f3c9
      </code>
     </div>
    </div>
    <div class="text-center">
     Performance &amp; security by
     <a href="https://www.cloudflare.com?utm_source=challenge&amp;utm_campaign=m" rel="noopener noreferrer" target="_blank">
      Cloudflare
     </a>
    </div>
   </div>
  </div>
 </body>
</html>


'''


