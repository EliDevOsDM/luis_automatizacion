Actua como un experto en desarrollador de aplicaciones de escriorio en python, necesito que realices lo siguiente, crea una ventana con python para esta automatizcaion, escanea el config.xslx, ahi tienes 3 hojas, una de credenciales, esa son de usuario y contraseña, que usaras en este sitio web

https://sgdea.mineducacion.gov.co/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/Home/Corporativo

<head><style>body {transition: opacity ease-in 0.2s; } 
body[unresolved] {opacity: 0; display: block; overflow: hidden; position: relative; } 
</style>
    <meta http-equiv="content-type" content="text/html;charset=UTF-8">
    <meta charset="utf-8">
    <title>Iniciar sesión por dominio - TMS Versión 2025.00.013</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="description" content="TMS,workflow,document management">
    <meta name="author" content="Sertisoft S.A.S">
    <link href="/TMS.Solution.MENGESDOC/favicon.ico" rel="shortcut icon" type="image/x-icon">
 
    <!--[if lt IE 9]>
        <script src="~/Scripts/html5shiv.min.js"></script>
        <script src="~/Scripts/respond.min.js"></script>
    <![endif]-->
    
    <link href="/TMS.Solution.MENGESDOC/font-awesome/css?v=3iEv8vqPidB6TVfgNOGrLoJr-SPH_mV3YwpggEk2_ao1" rel="stylesheet">

    <link href="/TMS.Solution.MENGESDOC/Content/sweetalert.css" rel="stylesheet">

    <link href="/TMS.Solution.MENGESDOC/Content/portal/gov/general.css" rel="stylesheet">

    <link href="/TMS.Solution.MENGESDOC/Content/portal/gov/v2/cdn.min.css" rel="stylesheet">

    <link href="/TMS.Solution.MENGESDOC/Content/portal/gov/v3/cdn.min.css" rel="stylesheet">

    <link href="/TMS.Solution.MENGESDOC/Content/Portal/src/altocontraste.css" rel="stylesheet">


    <style></style>
    <style type="text/css">
        .modal-open .container-fluid, .modal-open .container {
            -webkit-filter: none;
            filter: none;
        }

        .img-carrusel {
            background-position: top left;
            background-size: cover;
            min-height: 300px;
        }

        .content-logo {
            background-color: transparent;
        }
        /* Volver arriba */

        .volver-arriba-govco {
            color: #FFFFFF;
            width: 54px;
            height: 54px;
            border-radius: 50%;
            background: #3366CC 0% 0% no-repeat padding-box;
            box-shadow: 4px 4px 6px #00000029;
            transform: translateX(0);
            transition: all 300ms;
            text-align: center;
            border-width: 0px;
            display: none;
            position: fixed;
            bottom: 30px; /* distancia desde abajo */
            right: 30px; /* distancia desde la derecha */
            z-index: 9999; /* siempre por encima */
        }


            .volver-arriba-govco::before {
                content: "";
                display: inline-block;
                width: 36px;
                height: 36px;
                margin-top: 8px;
                margin-bottom: 8px;
                border-radius: 50%;
                background-color: #FFF;
                background-repeat: no-repeat;
                background-size: 70%;
                background-position: center;
                background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='57.07' height='35.61' viewBox='0 0 57.07 35.61'><polygon points='50 35.61 28.54 14.14 7.07 35.61 0 28.54 28.54 0 57.07 28.54 50 35.61' style='fill:%233366cc;'/></svg>");
            }


            .volver-arriba-govco:hover {
                color: white;
                width: 118px;
                height: 54px;
                background: #004884 0% 0% no-repeat padding-box;
                box-shadow: 4px 4px 6px #00000029;
                border-radius: 27px 10px 10px 27px;
                text-align: center;
                border-width: 0px;
                text-align: left;
                /*transform: translateX(-50%);*/
                transition: all 300ms;
            }

                .volver-arriba-govco:hover::before {
                    content: "";
                    display: inline-block;
                    width: 36px; /* Igual al estado normal */
                    height: 36px;
                    margin-top: 8px;
                    margin-bottom: 8px;
                    margin-left: 6px;
                    background-repeat: no-repeat;
                    background-size: 70%;
                    /* SVG igual al original */
                    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='57.07' height='35.61' viewBox='0 0 57.07 35.61'><polygon points='50 35.61 28.54 14.14 7.07 35.61 0 28.54 28.54 0 57.07 28.54 50 35.61' style='fill:%233366cc;'/></svg>");
                }

                .volver-arriba-govco:hover::after {
                    content: "Volver arriba";
                    color: white;
                    position: absolute;
                    text-align: center;
                    font: normal normal medium 16px/19px Work Sans;
                    letter-spacing: 0px;
                    margin-top: 8px;
                    margin-left: 8px;
                    line-height: 1.2;
                    width: 52px;
                    height: 42px;
                    transform: none;
                }


            .volver-arriba-govco:focus,
            .volver-arriba-govco:active {
                color: white;
                width: 118px;
                height: 54px;
                background: #004884 0% 0% no-repeat padding-box;
                box-shadow: 4px 4px 6px #00000029;
                border-radius: 27px 10px 10px 27px;
                border-width: 0px;
                text-align: left;
                outline: 7px double black !important;
                /*transform: translateX(-50%);*/
                transition: all 300ms;
            }

                .volver-arriba-govco:focus::before,
                .volver-arriba-govco:active::before {
                    font-family: "govco-fontv2";
                    content: "\e8b4";
                    display: inline-block;
                    font-weight: 900;
                    line-height: 1;
                    font-size: 36px;
                    margin-top: 8px;
                    margin-bottom: 8px;
                    margin-left: 6px;
                }

                .volver-arriba-govco:focus::before,
                .volver-arriba-govco:active::before {
                    content: "";
                    display: inline-block;
                    width: 36px; /* Igual que en los otros estados */
                    height: 36px;
                    margin-top: 8px;
                    margin-bottom: 8px;
                    margin-left: 6px;
                    background-repeat: no-repeat;
                    background-size: 70%;
                    /* Mismo SVG */
                    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='57.07' height='35.61' viewBox='0 0 57.07 35.61'><polygon points='50 35.61 28.54 14.14 7.07 35.61 0 28.54 28.54 0 57.07 28.54 50 35.61' style='fill:%233366cc;'/></svg>");
                }

        .btn-login-provider {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            width: 100%;
            height: 48px;
            border: 1px solid #D0D7E2;
            border-radius: 8px;
            background: #fff;
            color: #003770;
            font-weight: 600;
            transition: all .2s ease;
        }

            .btn-login-provider:hover {
                background: #F5F8FF;
                border-color: #3366CC;
            }

            .btn-login-provider img {
                width: 20px;
                height: 20px;
            }

        .externalBtn {
            border-radius: 30px !important;
            min-width: 162px !important;
        }

        .text-center-login {
            display: block;
            text-align: center;
        }

        .form-login-externo {
            padding: 12px 42px;
        }
    </style>

<style type="text/css">[data-sonner-toaster][dir=ltr],html[dir=ltr]{--toast-icon-margin-start:-3px;--toast-icon-margin-end:4px;--toast-svg-margin-start:-1px;--toast-svg-margin-end:0px;--toast-button-margin-start:auto;--toast-button-margin-end:0;--toast-close-button-start:0;--toast-close-button-end:unset;--toast-close-button-transform:translate(-35%, -35%)}[data-sonner-toaster][dir=rtl],html[dir=rtl]{--toast-icon-margin-start:4px;--toast-icon-margin-end:-3px;--toast-svg-margin-start:0px;--toast-svg-margin-end:-1px;--toast-button-margin-start:0;--toast-button-margin-end:auto;--toast-close-button-start:unset;--toast-close-button-end:0;--toast-close-button-transform:translate(35%, -35%)}[data-sonner-toaster]{position:fixed;width:var(--width);font-family:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;--gray1:hsl(0, 0%, 99%);--gray2:hsl(0, 0%, 97.3%);--gray3:hsl(0, 0%, 95.1%);--gray4:hsl(0, 0%, 93%);--gray5:hsl(0, 0%, 90.9%);--gray6:hsl(0, 0%, 88.7%);--gray7:hsl(0, 0%, 85.8%);--gray8:hsl(0, 0%, 78%);--gray9:hsl(0, 0%, 56.1%);--gray10:hsl(0, 0%, 52.3%);--gray11:hsl(0, 0%, 43.5%);--gray12:hsl(0, 0%, 9%);--border-radius:8px;box-sizing:border-box;padding:0;margin:0;list-style:none;outline:0;z-index:999999999;transition:transform .4s ease}@media (hover:none) and (pointer:coarse){[data-sonner-toaster][data-lifted=true]{transform:none}}[data-sonner-toaster][data-x-position=right]{right:var(--offset-right)}[data-sonner-toaster][data-x-position=left]{left:var(--offset-left)}[data-sonner-toaster][data-x-position=center]{left:50%;transform:translateX(-50%)}[data-sonner-toaster][data-y-position=top]{top:var(--offset-top)}[data-sonner-toaster][data-y-position=bottom]{bottom:var(--offset-bottom)}[data-sonner-toast]{--y:translateY(100%);--lift-amount:calc(var(--lift) * var(--gap));z-index:var(--z-index);position:absolute;opacity:0;transform:var(--y);touch-action:none;transition:transform .4s,opacity .4s,height .4s,box-shadow .2s;box-sizing:border-box;outline:0;overflow-wrap:anywhere}[data-sonner-toast][data-styled=true]{padding:16px;background:var(--normal-bg);border:1px solid var(--normal-border);color:var(--normal-text);border-radius:var(--border-radius);box-shadow:0 4px 12px rgba(0,0,0,.1);width:var(--width);font-size:13px;display:flex;align-items:center;gap:6px}[data-sonner-toast]:focus-visible{box-shadow:0 4px 12px rgba(0,0,0,.1),0 0 0 2px rgba(0,0,0,.2)}[data-sonner-toast][data-y-position=top]{top:0;--y:translateY(-100%);--lift:1;--lift-amount:calc(1 * var(--gap))}[data-sonner-toast][data-y-position=bottom]{bottom:0;--y:translateY(100%);--lift:-1;--lift-amount:calc(var(--lift) * var(--gap))}[data-sonner-toast][data-styled=true] [data-description]{font-weight:400;line-height:1.4;color:#3f3f3f}[data-rich-colors=true][data-sonner-toast][data-styled=true] [data-description]{color:inherit}[data-sonner-toaster][data-sonner-theme=dark] [data-description]{color:#e8e8e8}[data-sonner-toast][data-styled=true] [data-title]{font-weight:500;line-height:1.5;color:inherit}[data-sonner-toast][data-styled=true] [data-icon]{display:flex;height:16px;width:16px;position:relative;justify-content:flex-start;align-items:center;flex-shrink:0;margin-left:var(--toast-icon-margin-start);margin-right:var(--toast-icon-margin-end)}[data-sonner-toast][data-promise=true] [data-icon]>svg{opacity:0;transform:scale(.8);transform-origin:center;animation:sonner-fade-in .3s ease forwards}[data-sonner-toast][data-styled=true] [data-icon]>*{flex-shrink:0}[data-sonner-toast][data-styled=true] [data-icon] svg{margin-left:var(--toast-svg-margin-start);margin-right:var(--toast-svg-margin-end)}[data-sonner-toast][data-styled=true] [data-content]{display:flex;flex-direction:column;gap:2px}[data-sonner-toast][data-styled=true] [data-button]{border-radius:4px;padding-left:8px;padding-right:8px;height:24px;font-size:12px;color:var(--normal-bg);background:var(--normal-text);margin-left:var(--toast-button-margin-start);margin-right:var(--toast-button-margin-end);border:none;font-weight:500;cursor:pointer;outline:0;display:flex;align-items:center;flex-shrink:0;transition:opacity .4s,box-shadow .2s}[data-sonner-toast][data-styled=true] [data-button]:focus-visible{box-shadow:0 0 0 2px rgba(0,0,0,.4)}[data-sonner-toast][data-styled=true] [data-button]:first-of-type{margin-left:var(--toast-button-margin-start);margin-right:var(--toast-button-margin-end)}[data-sonner-toast][data-styled=true] [data-cancel]{color:var(--normal-text);background:rgba(0,0,0,.08)}[data-sonner-toaster][data-sonner-theme=dark] [data-sonner-toast][data-styled=true] [data-cancel]{background:rgba(255,255,255,.3)}[data-sonner-toast][data-styled=true] [data-close-button]{position:absolute;left:var(--toast-close-button-start);right:var(--toast-close-button-end);top:0;height:20px;width:20px;display:flex;justify-content:center;align-items:center;padding:0;color:var(--gray12);background:var(--normal-bg);border:1px solid var(--gray4);transform:var(--toast-close-button-transform);border-radius:50%;cursor:pointer;z-index:1;transition:opacity .1s,background .2s,border-color .2s}[data-sonner-toast][data-styled=true] [data-close-button]:focus-visible{box-shadow:0 4px 12px rgba(0,0,0,.1),0 0 0 2px rgba(0,0,0,.2)}[data-sonner-toast][data-styled=true] [data-disabled=true]{cursor:not-allowed}[data-sonner-toast][data-styled=true]:hover [data-close-button]:hover{background:var(--gray2);border-color:var(--gray5)}[data-sonner-toast][data-swiping=true]::before{content:'';position:absolute;left:-100%;right:-100%;height:100%;z-index:-1}[data-sonner-toast][data-y-position=top][data-swiping=true]::before{bottom:50%;transform:scaleY(3) translateY(50%)}[data-sonner-toast][data-y-position=bottom][data-swiping=true]::before{top:50%;transform:scaleY(3) translateY(-50%)}[data-sonner-toast][data-swiping=false][data-removed=true]::before{content:'';position:absolute;inset:0;transform:scaleY(2)}[data-sonner-toast][data-expanded=true]::after{content:'';position:absolute;left:0;height:calc(var(--gap) + 1px);bottom:100%;width:100%}[data-sonner-toast][data-mounted=true]{--y:translateY(0);opacity:1}[data-sonner-toast][data-expanded=false][data-front=false]{--scale:var(--toasts-before) * 0.05 + 1;--y:translateY(calc(var(--lift-amount) * var(--toasts-before))) scale(calc(-1 * var(--scale)));height:var(--front-toast-height)}[data-sonner-toast]>*{transition:opacity .4s}[data-sonner-toast][data-x-position=right]{right:0}[data-sonner-toast][data-x-position=left]{left:0}[data-sonner-toast][data-expanded=false][data-front=false][data-styled=true]>*{opacity:0}[data-sonner-toast][data-visible=false]{opacity:0;pointer-events:none}[data-sonner-toast][data-mounted=true][data-expanded=true]{--y:translateY(calc(var(--lift) * var(--offset)));height:var(--initial-height)}[data-sonner-toast][data-removed=true][data-front=true][data-swipe-out=false]{--y:translateY(calc(var(--lift) * -100%));opacity:0}[data-sonner-toast][data-removed=true][data-front=false][data-swipe-out=false][data-expanded=true]{--y:translateY(calc(var(--lift) * var(--offset) + var(--lift) * -100%));opacity:0}[data-sonner-toast][data-removed=true][data-front=false][data-swipe-out=false][data-expanded=false]{--y:translateY(40%);opacity:0;transition:transform .5s,opacity .2s}[data-sonner-toast][data-removed=true][data-front=false]::before{height:calc(var(--initial-height) + 20%)}[data-sonner-toast][data-swiping=true]{transform:var(--y) translateY(var(--swipe-amount-y,0)) translateX(var(--swipe-amount-x,0));transition:none}[data-sonner-toast][data-swiped=true]{user-select:none}[data-sonner-toast][data-swipe-out=true][data-y-position=bottom],[data-sonner-toast][data-swipe-out=true][data-y-position=top]{animation-duration:.2s;animation-timing-function:ease-out;animation-fill-mode:forwards}[data-sonner-toast][data-swipe-out=true][data-swipe-direction=left]{animation-name:swipe-out-left}[data-sonner-toast][data-swipe-out=true][data-swipe-direction=right]{animation-name:swipe-out-right}[data-sonner-toast][data-swipe-out=true][data-swipe-direction=up]{animation-name:swipe-out-up}[data-sonner-toast][data-swipe-out=true][data-swipe-direction=down]{animation-name:swipe-out-down}@keyframes swipe-out-left{from{transform:var(--y) translateX(var(--swipe-amount-x));opacity:1}to{transform:var(--y) translateX(calc(var(--swipe-amount-x) - 100%));opacity:0}}@keyframes swipe-out-right{from{transform:var(--y) translateX(var(--swipe-amount-x));opacity:1}to{transform:var(--y) translateX(calc(var(--swipe-amount-x) + 100%));opacity:0}}@keyframes swipe-out-up{from{transform:var(--y) translateY(var(--swipe-amount-y));opacity:1}to{transform:var(--y) translateY(calc(var(--swipe-amount-y) - 100%));opacity:0}}@keyframes swipe-out-down{from{transform:var(--y) translateY(var(--swipe-amount-y));opacity:1}to{transform:var(--y) translateY(calc(var(--swipe-amount-y) + 100%));opacity:0}}@media (max-width:600px){[data-sonner-toaster]{position:fixed;right:var(--mobile-offset-right);left:var(--mobile-offset-left);width:100%}[data-sonner-toaster][dir=rtl]{left:calc(var(--mobile-offset-left) * -1)}[data-sonner-toaster] [data-sonner-toast]{left:0;right:0;width:calc(100% - var(--mobile-offset-left) * 2)}[data-sonner-toaster][data-x-position=left]{left:var(--mobile-offset-left)}[data-sonner-toaster][data-y-position=bottom]{bottom:var(--mobile-offset-bottom)}[data-sonner-toaster][data-y-position=top]{top:var(--mobile-offset-top)}[data-sonner-toaster][data-x-position=center]{left:var(--mobile-offset-left);right:var(--mobile-offset-right);transform:none}}[data-sonner-toaster][data-sonner-theme=light]{--normal-bg:#fff;--normal-border:var(--gray4);--normal-text:var(--gray12);--success-bg:hsl(143, 85%, 96%);--success-border:hsl(145, 92%, 87%);--success-text:hsl(140, 100%, 27%);--info-bg:hsl(208, 100%, 97%);--info-border:hsl(221, 91%, 93%);--info-text:hsl(210, 92%, 45%);--warning-bg:hsl(49, 100%, 97%);--warning-border:hsl(49, 91%, 84%);--warning-text:hsl(31, 92%, 45%);--error-bg:hsl(359, 100%, 97%);--error-border:hsl(359, 100%, 94%);--error-text:hsl(360, 100%, 45%)}[data-sonner-toaster][data-sonner-theme=light] [data-sonner-toast][data-invert=true]{--normal-bg:#000;--normal-border:hsl(0, 0%, 20%);--normal-text:var(--gray1)}[data-sonner-toaster][data-sonner-theme=dark] [data-sonner-toast][data-invert=true]{--normal-bg:#fff;--normal-border:var(--gray3);--normal-text:var(--gray12)}[data-sonner-toaster][data-sonner-theme=dark]{--normal-bg:#000;--normal-bg-hover:hsl(0, 0%, 12%);--normal-border:hsl(0, 0%, 20%);--normal-border-hover:hsl(0, 0%, 25%);--normal-text:var(--gray1);--success-bg:hsl(150, 100%, 6%);--success-border:hsl(147, 100%, 12%);--success-text:hsl(150, 86%, 65%);--info-bg:hsl(215, 100%, 6%);--info-border:hsl(223, 43%, 17%);--info-text:hsl(216, 87%, 65%);--warning-bg:hsl(64, 100%, 6%);--warning-border:hsl(60, 100%, 9%);--warning-text:hsl(46, 87%, 65%);--error-bg:hsl(358, 76%, 10%);--error-border:hsl(357, 89%, 16%);--error-text:hsl(358, 100%, 81%)}[data-sonner-toaster][data-sonner-theme=dark] [data-sonner-toast] [data-close-button]{background:var(--normal-bg);border-color:var(--normal-border);color:var(--normal-text)}[data-sonner-toaster][data-sonner-theme=dark] [data-sonner-toast] [data-close-button]:hover{background:var(--normal-bg-hover);border-color:var(--normal-border-hover)}[data-rich-colors=true][data-sonner-toast][data-type=success]{background:var(--success-bg);border-color:var(--success-border);color:var(--success-text)}[data-rich-colors=true][data-sonner-toast][data-type=success] [data-close-button]{background:var(--success-bg);border-color:var(--success-border);color:var(--success-text)}[data-rich-colors=true][data-sonner-toast][data-type=info]{background:var(--info-bg);border-color:var(--info-border);color:var(--info-text)}[data-rich-colors=true][data-sonner-toast][data-type=info] [data-close-button]{background:var(--info-bg);border-color:var(--info-border);color:var(--info-text)}[data-rich-colors=true][data-sonner-toast][data-type=warning]{background:var(--warning-bg);border-color:var(--warning-border);color:var(--warning-text)}[data-rich-colors=true][data-sonner-toast][data-type=warning] [data-close-button]{background:var(--warning-bg);border-color:var(--warning-border);color:var(--warning-text)}[data-rich-colors=true][data-sonner-toast][data-type=error]{background:var(--error-bg);border-color:var(--error-border);color:var(--error-text)}[data-rich-colors=true][data-sonner-toast][data-type=error] [data-close-button]{background:var(--error-bg);border-color:var(--error-border);color:var(--error-text)}.sonner-loading-wrapper{--size:16px;height:var(--size);width:var(--size);position:absolute;inset:0;z-index:10}.sonner-loading-wrapper[data-visible=false]{transform-origin:center;animation:sonner-fade-out .2s ease forwards}.sonner-spinner{position:relative;top:50%;left:50%;height:var(--size);width:var(--size)}.sonner-loading-bar{animation:sonner-spin 1.2s linear infinite;background:var(--gray11);border-radius:6px;height:8%;left:-10%;position:absolute;top:-3.9%;width:24%}.sonner-loading-bar:first-child{animation-delay:-1.2s;transform:rotate(.0001deg) translate(146%)}.sonner-loading-bar:nth-child(2){animation-delay:-1.1s;transform:rotate(30deg) translate(146%)}.sonner-loading-bar:nth-child(3){animation-delay:-1s;transform:rotate(60deg) translate(146%)}.sonner-loading-bar:nth-child(4){animation-delay:-.9s;transform:rotate(90deg) translate(146%)}.sonner-loading-bar:nth-child(5){animation-delay:-.8s;transform:rotate(120deg) translate(146%)}.sonner-loading-bar:nth-child(6){animation-delay:-.7s;transform:rotate(150deg) translate(146%)}.sonner-loading-bar:nth-child(7){animation-delay:-.6s;transform:rotate(180deg) translate(146%)}.sonner-loading-bar:nth-child(8){animation-delay:-.5s;transform:rotate(210deg) translate(146%)}.sonner-loading-bar:nth-child(9){animation-delay:-.4s;transform:rotate(240deg) translate(146%)}.sonner-loading-bar:nth-child(10){animation-delay:-.3s;transform:rotate(270deg) translate(146%)}.sonner-loading-bar:nth-child(11){animation-delay:-.2s;transform:rotate(300deg) translate(146%)}.sonner-loading-bar:nth-child(12){animation-delay:-.1s;transform:rotate(330deg) translate(146%)}@keyframes sonner-fade-in{0%{opacity:0;transform:scale(.8)}100%{opacity:1;transform:scale(1)}}@keyframes sonner-fade-out{0%{opacity:1;transform:scale(1)}100%{opacity:0;transform:scale(.8)}}@keyframes sonner-spin{0%{opacity:1}100%{opacity:.15}}@media (prefers-reduced-motion){.sonner-loading-bar,[data-sonner-toast],[data-sonner-toast]>*{transition:none!important;animation:none!important}}.sonner-loader{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);transform-origin:center;transition:opacity .2s,transform .2s}.sonner-loader[data-visible=false]{opacity:0;transform:scale(.8) translate(-50%,-50%)}</style></head>


de ahi saca los dos box de usuario y contraseña y lo llenas automaticamente




Eso te llevara a esta pagina 
<head><style>body {transition: opacity ease-in 0.2s; } 
body[unresolved] {opacity: 0; display: block; overflow: hidden; position: relative; } 
</style>
    <meta http-equiv="content-type" content="text/html;charset=UTF-8">
    <meta charset="utf-8">
    <title>TMS - TMS Versión 2025.00.013</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="description" content="TMS,workflow,document management">
    <meta name="author" content="Sertisoft S.A.S">
    <link href="/TMS.Solution.MENGESDOC/favicon.ico" rel="shortcut icon" type="image/x-icon">
    <link href="/TMS.Solution.MENGESDOC/portal2s-b/css?v=0LNujXxxTX9zAP7SMqHlgkqxmYwgw0MOFYgULX08aoo1" rel="stylesheet">

    <link href="/TMS.Solution.MENGESDOC/portal2s/c/css?v=x3c09EBajKeQzsoUQcvQ6qWDDLoi0cvNNVLav7kLt6A1" rel="stylesheet">

    <!--[if lt IE 9]>
        <script src="~/Scripts/html5shiv.min.js"></script>
        <script src="~/Scripts/respond.min.js"></script>
    <![endif]-->
    
<style>
      
</style>
<style type="text/css">/* Chart.js */
@keyframes chartjs-render-animation{from{opacity:.99}to{opacity:1}}.chartjs-render-monitor{animation:chartjs-render-animation 1ms}.chartjs-size-monitor,.chartjs-size-monitor-expand,.chartjs-size-monitor-shrink{position:absolute;direction:ltr;left:0;top:0;right:0;bottom:0;overflow:hidden;pointer-events:none;visibility:hidden;z-index:-1}.chartjs-size-monitor-expand>div{position:absolute;width:1000000px;height:1000000px;left:0;top:0}.chartjs-size-monitor-shrink>div{position:absolute;width:200%;height:200%;left:0;top:0}</style><style type="text/css">[data-sonner-toaster][dir=ltr],html[dir=ltr]{--toast-icon-margin-start:-3px;--toast-icon-margin-end:4px;--toast-svg-margin-start:-1px;--toast-svg-margin-end:0px;--toast-button-margin-start:auto;--toast-button-margin-end:0;--toast-close-button-start:0;--toast-close-button-end:unset;--toast-close-button-transform:translate(-35%, -35%)}[data-sonner-toaster][dir=rtl],html[dir=rtl]{--toast-icon-margin-start:4px;--toast-icon-margin-end:-3px;--toast-svg-margin-start:0px;--toast-svg-margin-end:-1px;--toast-button-margin-start:0;--toast-button-margin-end:auto;--toast-close-button-start:unset;--toast-close-button-end:0;--toast-close-button-transform:translate(35%, -35%)}[data-sonner-toaster]{position:fixed;width:var(--width);font-family:ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;--gray1:hsl(0, 0%, 99%);--gray2:hsl(0, 0%, 97.3%);--gray3:hsl(0, 0%, 95.1%);--gray4:hsl(0, 0%, 93%);--gray5:hsl(0, 0%, 90.9%);--gray6:hsl(0, 0%, 88.7%);--gray7:hsl(0, 0%, 85.8%);--gray8:hsl(0, 0%, 78%);--gray9:hsl(0, 0%, 56.1%);--gray10:hsl(0, 0%, 52.3%);--gray11:hsl(0, 0%, 43.5%);--gray12:hsl(0, 0%, 9%);--border-radius:8px;box-sizing:border-box;padding:0;margin:0;list-style:none;outline:0;z-index:999999999;transition:transform .4s ease}@media (hover:none) and (pointer:coarse){[data-sonner-toaster][data-lifted=true]{transform:none}}[data-sonner-toaster][data-x-position=right]{right:var(--offset-right)}[data-sonner-toaster][data-x-position=left]{left:var(--offset-left)}[data-sonner-toaster][data-x-position=center]{left:50%;transform:translateX(-50%)}[data-sonner-toaster][data-y-position=top]{top:var(--offset-top)}[data-sonner-toaster][data-y-position=bottom]{bottom:var(--offset-bottom)}[data-sonner-toast]{--y:translateY(100%);--lift-amount:calc(var(--lift) * var(--gap));z-index:var(--z-index);position:absolute;opacity:0;transform:var(--y);touch-action:none;transition:transform .4s,opacity .4s,height .4s,box-shadow .2s;box-sizing:border-box;outline:0;overflow-wrap:anywhere}[data-sonner-toast][data-styled=true]{padding:16px;background:var(--normal-bg);border:1px solid var(--normal-border);color:var(--normal-text);border-radius:var(--border-radius);box-shadow:0 4px 12px rgba(0,0,0,.1);width:var(--width);font-size:13px;display:flex;align-items:center;gap:6px}[data-sonner-toast]:focus-visible{box-shadow:0 4px 12px rgba(0,0,0,.1),0 0 0 2px rgba(0,0,0,.2)}[data-sonner-toast][data-y-position=top]{top:0;--y:translateY(-100%);--lift:1;--lift-amount:calc(1 * var(--gap))}[data-sonner-toast][data-y-position=bottom]{bottom:0;--y:translateY(100%);--lift:-1;--lift-amount:calc(var(--lift) * var(--gap))}[data-sonner-toast][data-styled=true] [data-description]{font-weight:400;line-height:1.4;color:#3f3f3f}[data-rich-colors=true][data-sonner-toast][data-styled=true] [data-description]{color:inherit}[data-sonner-toaster][data-sonner-theme=dark] [data-description]{color:#e8e8e8}[data-sonner-toast][data-styled=true] [data-title]{font-weight:500;line-height:1.5;color:inherit}[data-sonner-toast][data-styled=true] [data-icon]{display:flex;height:16px;width:16px;position:relative;justify-content:flex-start;align-items:center;flex-shrink:0;margin-left:var(--toast-icon-margin-start);margin-right:var(--toast-icon-margin-end)}[data-sonner-toast][data-promise=true] [data-icon]>svg{opacity:0;transform:scale(.8);transform-origin:center;animation:sonner-fade-in .3s ease forwards}[data-sonner-toast][data-styled=true] [data-icon]>*{flex-shrink:0}[data-sonner-toast][data-styled=true] [data-icon] svg{margin-left:var(--toast-svg-margin-start);margin-right:var(--toast-svg-margin-end)}[data-sonner-toast][data-styled=true] [data-content]{display:flex;flex-direction:column;gap:2px}[data-sonner-toast][data-styled=true] [data-button]{border-radius:4px;padding-left:8px;padding-right:8px;height:24px;font-size:12px;color:var(--normal-bg);background:var(--normal-text);margin-left:var(--toast-button-margin-start);margin-right:var(--toast-button-margin-end);border:none;font-weight:500;cursor:pointer;outline:0;display:flex;align-items:center;flex-shrink:0;transition:opacity .4s,box-shadow .2s}[data-sonner-toast][data-styled=true] [data-button]:focus-visible{box-shadow:0 0 0 2px rgba(0,0,0,.4)}[data-sonner-toast][data-styled=true] [data-button]:first-of-type{margin-left:var(--toast-button-margin-start);margin-right:var(--toast-button-margin-end)}[data-sonner-toast][data-styled=true] [data-cancel]{color:var(--normal-text);background:rgba(0,0,0,.08)}[data-sonner-toaster][data-sonner-theme=dark] [data-sonner-toast][data-styled=true] [data-cancel]{background:rgba(255,255,255,.3)}[data-sonner-toast][data-styled=true] [data-close-button]{position:absolute;left:var(--toast-close-button-start);right:var(--toast-close-button-end);top:0;height:20px;width:20px;display:flex;justify-content:center;align-items:center;padding:0;color:var(--gray12);background:var(--normal-bg);border:1px solid var(--gray4);transform:var(--toast-close-button-transform);border-radius:50%;cursor:pointer;z-index:1;transition:opacity .1s,background .2s,border-color .2s}[data-sonner-toast][data-styled=true] [data-close-button]:focus-visible{box-shadow:0 4px 12px rgba(0,0,0,.1),0 0 0 2px rgba(0,0,0,.2)}[data-sonner-toast][data-styled=true] [data-disabled=true]{cursor:not-allowed}[data-sonner-toast][data-styled=true]:hover [data-close-button]:hover{background:var(--gray2);border-color:var(--gray5)}[data-sonner-toast][data-swiping=true]::before{content:'';position:absolute;left:-100%;right:-100%;height:100%;z-index:-1}[data-sonner-toast][data-y-position=top][data-swiping=true]::before{bottom:50%;transform:scaleY(3) translateY(50%)}[data-sonner-toast][data-y-position=bottom][data-swiping=true]::before{top:50%;transform:scaleY(3) translateY(-50%)}[data-sonner-toast][data-swiping=false][data-removed=true]::before{content:'';position:absolute;inset:0;transform:scaleY(2)}[data-sonner-toast][data-expanded=true]::after{content:'';position:absolute;left:0;height:calc(var(--gap) + 1px);bottom:100%;width:100%}[data-sonner-toast][data-mounted=true]{--y:translateY(0);opacity:1}[data-sonner-toast][data-expanded=false][data-front=false]{--scale:var(--toasts-before) * 0.05 + 1;--y:translateY(calc(var(--lift-amount) * var(--toasts-before))) scale(calc(-1 * var(--scale)));height:var(--front-toast-height)}[data-sonner-toast]>*{transition:opacity .4s}[data-sonner-toast][data-x-position=right]{right:0}[data-sonner-toast][data-x-position=left]{left:0}[data-sonner-toast][data-expanded=false][data-front=false][data-styled=true]>*{opacity:0}[data-sonner-toast][data-visible=false]{opacity:0;pointer-events:none}[data-sonner-toast][data-mounted=true][data-expanded=true]{--y:translateY(calc(var(--lift) * var(--offset)));height:var(--initial-height)}[data-sonner-toast][data-removed=true][data-front=true][data-swipe-out=false]{--y:translateY(calc(var(--lift) * -100%));opacity:0}[data-sonner-toast][data-removed=true][data-front=false][data-swipe-out=false][data-expanded=true]{--y:translateY(calc(var(--lift) * var(--offset) + var(--lift) * -100%));opacity:0}[data-sonner-toast][data-removed=true][data-front=false][data-swipe-out=false][data-expanded=false]{--y:translateY(40%);opacity:0;transition:transform .5s,opacity .2s}[data-sonner-toast][data-removed=true][data-front=false]::before{height:calc(var(--initial-height) + 20%)}[data-sonner-toast][data-swiping=true]{transform:var(--y) translateY(var(--swipe-amount-y,0)) translateX(var(--swipe-amount-x,0));transition:none}[data-sonner-toast][data-swiped=true]{user-select:none}[data-sonner-toast][data-swipe-out=true][data-y-position=bottom],[data-sonner-toast][data-swipe-out=true][data-y-position=top]{animation-duration:.2s;animation-timing-function:ease-out;animation-fill-mode:forwards}[data-sonner-toast][data-swipe-out=true][data-swipe-direction=left]{animation-name:swipe-out-left}[data-sonner-toast][data-swipe-out=true][data-swipe-direction=right]{animation-name:swipe-out-right}[data-sonner-toast][data-swipe-out=true][data-swipe-direction=up]{animation-name:swipe-out-up}[data-sonner-toast][data-swipe-out=true][data-swipe-direction=down]{animation-name:swipe-out-down}@keyframes swipe-out-left{from{transform:var(--y) translateX(var(--swipe-amount-x));opacity:1}to{transform:var(--y) translateX(calc(var(--swipe-amount-x) - 100%));opacity:0}}@keyframes swipe-out-right{from{transform:var(--y) translateX(var(--swipe-amount-x));opacity:1}to{transform:var(--y) translateX(calc(var(--swipe-amount-x) + 100%));opacity:0}}@keyframes swipe-out-up{from{transform:var(--y) translateY(var(--swipe-amount-y));opacity:1}to{transform:var(--y) translateY(calc(var(--swipe-amount-y) - 100%));opacity:0}}@keyframes swipe-out-down{from{transform:var(--y) translateY(var(--swipe-amount-y));opacity:1}to{transform:var(--y) translateY(calc(var(--swipe-amount-y) + 100%));opacity:0}}@media (max-width:600px){[data-sonner-toaster]{position:fixed;right:var(--mobile-offset-right);left:var(--mobile-offset-left);width:100%}[data-sonner-toaster][dir=rtl]{left:calc(var(--mobile-offset-left) * -1)}[data-sonner-toaster] [data-sonner-toast]{left:0;right:0;width:calc(100% - var(--mobile-offset-left) * 2)}[data-sonner-toaster][data-x-position=left]{left:var(--mobile-offset-left)}[data-sonner-toaster][data-y-position=bottom]{bottom:var(--mobile-offset-bottom)}[data-sonner-toaster][data-y-position=top]{top:var(--mobile-offset-top)}[data-sonner-toaster][data-x-position=center]{left:var(--mobile-offset-left);right:var(--mobile-offset-right);transform:none}}[data-sonner-toaster][data-sonner-theme=light]{--normal-bg:#fff;--normal-border:var(--gray4);--normal-text:var(--gray12);--success-bg:hsl(143, 85%, 96%);--success-border:hsl(145, 92%, 87%);--success-text:hsl(140, 100%, 27%);--info-bg:hsl(208, 100%, 97%);--info-border:hsl(221, 91%, 93%);--info-text:hsl(210, 92%, 45%);--warning-bg:hsl(49, 100%, 97%);--warning-border:hsl(49, 91%, 84%);--warning-text:hsl(31, 92%, 45%);--error-bg:hsl(359, 100%, 97%);--error-border:hsl(359, 100%, 94%);--error-text:hsl(360, 100%, 45%)}[data-sonner-toaster][data-sonner-theme=light] [data-sonner-toast][data-invert=true]{--normal-bg:#000;--normal-border:hsl(0, 0%, 20%);--normal-text:var(--gray1)}[data-sonner-toaster][data-sonner-theme=dark] [data-sonner-toast][data-invert=true]{--normal-bg:#fff;--normal-border:var(--gray3);--normal-text:var(--gray12)}[data-sonner-toaster][data-sonner-theme=dark]{--normal-bg:#000;--normal-bg-hover:hsl(0, 0%, 12%);--normal-border:hsl(0, 0%, 20%);--normal-border-hover:hsl(0, 0%, 25%);--normal-text:var(--gray1);--success-bg:hsl(150, 100%, 6%);--success-border:hsl(147, 100%, 12%);--success-text:hsl(150, 86%, 65%);--info-bg:hsl(215, 100%, 6%);--info-border:hsl(223, 43%, 17%);--info-text:hsl(216, 87%, 65%);--warning-bg:hsl(64, 100%, 6%);--warning-border:hsl(60, 100%, 9%);--warning-text:hsl(46, 87%, 65%);--error-bg:hsl(358, 76%, 10%);--error-border:hsl(357, 89%, 16%);--error-text:hsl(358, 100%, 81%)}[data-sonner-toaster][data-sonner-theme=dark] [data-sonner-toast] [data-close-button]{background:var(--normal-bg);border-color:var(--normal-border);color:var(--normal-text)}[data-sonner-toaster][data-sonner-theme=dark] [data-sonner-toast] [data-close-button]:hover{background:var(--normal-bg-hover);border-color:var(--normal-border-hover)}[data-rich-colors=true][data-sonner-toast][data-type=success]{background:var(--success-bg);border-color:var(--success-border);color:var(--success-text)}[data-rich-colors=true][data-sonner-toast][data-type=success] [data-close-button]{background:var(--success-bg);border-color:var(--success-border);color:var(--success-text)}[data-rich-colors=true][data-sonner-toast][data-type=info]{background:var(--info-bg);border-color:var(--info-border);color:var(--info-text)}[data-rich-colors=true][data-sonner-toast][data-type=info] [data-close-button]{background:var(--info-bg);border-color:var(--info-border);color:var(--info-text)}[data-rich-colors=true][data-sonner-toast][data-type=warning]{background:var(--warning-bg);border-color:var(--warning-border);color:var(--warning-text)}[data-rich-colors=true][data-sonner-toast][data-type=warning] [data-close-button]{background:var(--warning-bg);border-color:var(--warning-border);color:var(--warning-text)}[data-rich-colors=true][data-sonner-toast][data-type=error]{background:var(--error-bg);border-color:var(--error-border);color:var(--error-text)}[data-rich-colors=true][data-sonner-toast][data-type=error] [data-close-button]{background:var(--error-bg);border-color:var(--error-border);color:var(--error-text)}.sonner-loading-wrapper{--size:16px;height:var(--size);width:var(--size);position:absolute;inset:0;z-index:10}.sonner-loading-wrapper[data-visible=false]{transform-origin:center;animation:sonner-fade-out .2s ease forwards}.sonner-spinner{position:relative;top:50%;left:50%;height:var(--size);width:var(--size)}.sonner-loading-bar{animation:sonner-spin 1.2s linear infinite;background:var(--gray11);border-radius:6px;height:8%;left:-10%;position:absolute;top:-3.9%;width:24%}.sonner-loading-bar:first-child{animation-delay:-1.2s;transform:rotate(.0001deg) translate(146%)}.sonner-loading-bar:nth-child(2){animation-delay:-1.1s;transform:rotate(30deg) translate(146%)}.sonner-loading-bar:nth-child(3){animation-delay:-1s;transform:rotate(60deg) translate(146%)}.sonner-loading-bar:nth-child(4){animation-delay:-.9s;transform:rotate(90deg) translate(146%)}.sonner-loading-bar:nth-child(5){animation-delay:-.8s;transform:rotate(120deg) translate(146%)}.sonner-loading-bar:nth-child(6){animation-delay:-.7s;transform:rotate(150deg) translate(146%)}.sonner-loading-bar:nth-child(7){animation-delay:-.6s;transform:rotate(180deg) translate(146%)}.sonner-loading-bar:nth-child(8){animation-delay:-.5s;transform:rotate(210deg) translate(146%)}.sonner-loading-bar:nth-child(9){animation-delay:-.4s;transform:rotate(240deg) translate(146%)}.sonner-loading-bar:nth-child(10){animation-delay:-.3s;transform:rotate(270deg) translate(146%)}.sonner-loading-bar:nth-child(11){animation-delay:-.2s;transform:rotate(300deg) translate(146%)}.sonner-loading-bar:nth-child(12){animation-delay:-.1s;transform:rotate(330deg) translate(146%)}@keyframes sonner-fade-in{0%{opacity:0;transform:scale(.8)}100%{opacity:1;transform:scale(1)}}@keyframes sonner-fade-out{0%{opacity:1;transform:scale(1)}100%{opacity:0;transform:scale(.8)}}@keyframes sonner-spin{0%{opacity:1}100%{opacity:.15}}@media (prefers-reduced-motion){.sonner-loading-bar,[data-sonner-toast],[data-sonner-toast]>*{transition:none!important;animation:none!important}}.sonner-loader{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);transform-origin:center;transition:opacity .2s,transform .2s}.sonner-loader[data-visible=false]{opacity:0;transform:scale(.8) translate(-50%,-50%)}</style></head>



le das click a este elemento
<canvas class="bar-secuencia-abiertas chartjs-render-monitor" max-width="100" max-height="100" id="barSecuenciaAbiertas1" width="308" height="154" style="display: block; width: 308px; height: 154px; cursor: default;"></canvas>


eso te lleva a esta parte
<body class="  pace-done" cz-shortcut-listen="true"><div class="pace  pace-inactive"><div class="pace-progress" data-progress-text="100%" data-progress="99" style="transform: translate3d(100%, 0px, 0px);">
  <div class="pace-progress-inner"></div>
</div>
<div class="pace-activity"></div></div>
    <nav class="navbar navbar-expand-lg navbar-light bg-white shadow-sm p-0 text-dark fixed-top">
        <div class="header-title TMSTituloBg">
                    <div>
                        <span style="font-size:38px;" class="TMSTituloTxt">
                            SGDEA
                        </span>

                    </div>

        </div>

        <ul class="navbar-nav">
            <li class="nav-item active">
                <a class="nav-link pl-3 menu-tms-button" id="menuTMSc">
                    <i class="fa fa-bars icon-header" aria-hidden="true"></i>
                </a>
            </li>
        </ul>
        <a class="navbar-brand p-0" href="/TMS.Solution.MENGESDOC/">
            <div class="TMSTituloImg TMSTituloBg1 logo-header logo-header-left"></div>
            <div class="TMSTituloBg1 TMSTituloImg2 logo-header logo-header-right" style="width: 200px;"></div>
        </a>
        <button class="navbar-toggler border-0" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="fa fa-bars"></span>
        </button>
        <div class="collapse navbar-collapse p-2" id="navbarSupportedContent">
            <span class="navbar-text py-0 pr-2 ml-auto text-dark text-md-right" style="line-height: .9;">
                <small class="header-text">
                        <strong>DIANA CAMILA ZAPATA VALENCIA</strong><br>
Oficina Asesora Jurídica<br>
MINISTERIO DE EDUCACIÓN NACIONAL                </small>
            </span>
            <ul class="navbar-nav">

                <li class="nav-item" id="BtnAyudaPortal">
                    <a class="nav-link" title="Ayuda" href="https://sgdea.mineducacion.gov.co/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/MAM/DocumentacionUsuario">
                        <i class="fa fa-question-circle-o icon-header" aria-hidden="true" style="color:#000 !important;"></i><span class="d-lg-none">Ayuda</span>
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/TMS.Solution.MENGESDOC/Account/Logout" id="logout" title="Cerrar sesión">
                        <i class="fa fa-power-off icon-header" aria-hidden="true" style="color:#000 !important;"></i> <span class="d-lg-none">Cerrar sesión</span>
                    </a>
                </li>
            </ul>
        </div>
    </nav>
    <div class="TMSTituloBg title-responsive px-2">
                <span class="TMSTituloTxt">SGDEA</span>

    </div>

    <div class="page-container row">
        <div class="page-sidebar " id="main-menu">
            <div class="scroll-wrapper page-sidebar-wrapper scrollbar-dynamic TMSTituloTxt" style="position: relative;"><div class="page-sidebar-wrapper scrollbar-dynamic TMSTituloTxt scroll-content" id="main-menu-wrapper" style="margin-bottom: 0px; margin-right: 0px;">

<ul class="menu-items">
    <li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MaM/TableroUsuario" title="Inicio - Mis asignadas"><i class="fa fa-home" aria-hidden="true"></i><span class="title">Inicio - Mis asignadas</span></a></li>
<li><a href="javascript:;" title="Consultar"><i class="fa fa-search-plus" aria-hidden="true"></i><span class="title">Consultar</span><span class="arrow open"></span></a><ul class="sub-menu" style="display: none;"><li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MAM/Consultar" title="Consulta solicitudes"><i class="fa fa-search" aria-hidden="true"></i><span class="title">Consulta solicitudes</span></a></li>
<li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MAM/Corr/ConsultarRecibidas" title="Comunicaciones recibidas"><i class="fa fa-search" aria-hidden="true"></i><span class="title">Comunicaciones recibidas</span></a></li>
<li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MAM/MEMO/ConsultarMemorando" title="Comunicaciones Internas"><i class="fa fa-envelope-o" aria-hidden="true"></i><span class="title">Comunicaciones Internas</span></a></li>
<li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MAM/Corr/ConsultarDocumentosMasivos?tipoConsulta=1" title="Comunicaciones internas masivas"><i class="fa fa-search-plus" aria-hidden="true"></i><span class="title">Comunicaciones internas masivas</span></a></li>
<li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MAM/Corr/ConsultarEnviadas" title="Comunicaciones enviadas"><i class="fa fa-send-o" aria-hidden="true"></i><span class="title">Comunicaciones enviadas</span></a></li>
<li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MAM/Corr/ConsultarDocumentosMasivos?tipoConsulta=2" title="Comunicaciones enviadas masivas"><i class="fa fa-search-plus" aria-hidden="true"></i><span class="title">Comunicaciones enviadas masivas</span></a></li>
<li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MAM/Corr/ConsultarDocumentosAvanzada" title="Consulta avanzada documentos"><i class="fa fa-search-plus" aria-hidden="true"></i><span class="title">Consulta avanzada documentos</span></a></li>
<li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MAM/TableroDocumentos" title="Documentos"><i class="fa fa-file-o" aria-hidden="true"></i><span class="title">Documentos</span></a></li>
<li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../VersionesDocumentoEditorRich/ControlDocumento" title="Control Documentos Respuesta en Blanco"><i class="fa fa-eye" aria-hidden="true"></i><span class="title">Control Documentos Respuesta en Blanco</span></a></li>
</ul></li>
<li><a href="javascript:;" title="Crear"><i class="fa fa-file-o" aria-hidden="true"></i><span class="title">Crear</span><span class="arrow open"></span></a><ul class="sub-menu" style="display: none;"><li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MAM/Corr/CrearDocumento?idTipoDoc=436" title="Comunicación de salida"><i class="fa fa-file-text-o" aria-hidden="true"></i><span class="title">Comunicación de salida</span></a></li>
<li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MAM/Corr/CrearDocumento?idTipoDoc=496" title="Comunicación de salida masiva"><i class="fa fa-files-o" aria-hidden="true"></i><span class="title">Comunicación de salida masiva</span></a></li>
<li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MAM/CORR/ConsultarRespuestasMasivas" title="Respuesta masiva"><i class="fa fa-files-o" aria-hidden="true"></i><span class="title">Respuesta masiva</span></a></li>
<li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MAM/Corr/CrearDocumento?idTipoDoc=516" title="Comunicación de salida (Múltiples Firmantes)"><i class="fa fa-file-text" aria-hidden="true"></i><span class="title">Comunicación de salida (Múltiples Firmantes)</span></a></li>
<li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MAM/Corr/CrearDocumento?idTipoDoc=438" title="Comunicación interna - Memorando"><i class="fa fa-file-word-o" aria-hidden="true"></i><span class="title">Comunicación interna - Memorando</span></a></li>
<li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MAM/Corr/CrearDocumento?idTipoDoc=514" title="Comunicación interna - Memorando masivo"><i class="fa fa-files-o" aria-hidden="true"></i><span class="title">Comunicación interna - Memorando masivo</span></a></li>
</ul></li>
<li><a href="javascript:;" title="Archivar"><i class="fa fa-folder-open" aria-hidden="true"></i><span class="title">Archivar</span><span class="arrow open"></span></a><ul class="sub-menu" style="display: none;"><li><a href="javascript:;" onclick="fnAccionTMS(this);" data-app="TMS" data-url="ModuloArchivistica/ArchivisticaPrincipal.asp_Inter_modulo=AR" title="Expedientes documentales"><i class="fa fa-folder-open-o" aria-hidden="true"></i><span class="title">Expedientes documentales</span></a></li>
<li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../MAM/archivo/solicitarexpediente" title="Solicitar préstamos de expedientes"><i class="fa fa-file-text" aria-hidden="true"></i><span class="title">Solicitar préstamos de expedientes</span></a></li>
</ul></li>
<li><a href="javascript:;" title="Plantillas electrónicas"><i class="fa fa-copy" aria-hidden="true"></i><span class="title">Plantillas electrónicas</span><span class="arrow open"></span></a><ul class="sub-menu" style="display: none;"><li><a href="/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/g/d/../../EditorDocumentalRich/TipoDocCrear?gidProceso=98F9AAB5-883B-43D0-B2F1-462875073A68" title="Creación de nuevos documentos"><i class="fa fa-list" aria-hidden="true"></i><span class="title">Creación de nuevos documentos</span></a></li>
</ul></li>

</ul>
                <div class="clearfix"></div>
            </div><div class="scroll-element scroll-x"><div class="scroll-element_outer">    <div class="scroll-element_size"></div>    <div class="scroll-element_track"></div>    <div class="scroll-bar" style="width: 0px; left: 0px;"></div></div></div><div class="scroll-element scroll-y"><div class="scroll-element_outer">    <div class="scroll-element_size"></div>    <div class="scroll-element_track"></div>    <div class="scroll-bar" style="height: 0px; top: 0px;"></div></div></div></div>
        </div>
        <div class="footer-widget">
            <a href="/TMS.Solution.MENGESDOC/" id="tmsPtHome" title="Inicio"><i class="fa fa-home" aria-hidden="true"></i></a>
            <a href="#" id="tmsPtZoom" title="Cambiar tamaño de la letra"><i class="fa fa-search-plus" aria-hidden="true"></i></a>
            <a href="#" id="tmsPtContr" title="Cambiar el esquema de color, activando o inactivando contrastes altos"><i class="fa fa-sun-o" aria-hidden="true"></i></a>
                    <a href="#" id="tmsPtApps" title="Cambiar la aplicacion existente"><i class="fa fa-th" aria-hidden="true"></i></a>

        </div>
        <div class="page-content">
            <div class="content" id="TMSContainer">
                <!-- BreadCrumbs stack is empty -->
                
<link href="/TMS.Solution.MENGESDOC/MaM/css/General.css" rel="stylesheet">


<div class="container-fluid" id="breadcrumbMisAsignadas">
    <div class="row breadcrumb-container">
        <div class="col-sm-12 col-md-8">
            <ol class="breadcrumb-gestion">
            <li class="breadcrumb-item" data-id="TableroAPP"><a href="#" id="verTableroAPP"><span>Inicio<span></span></span></a></li><li class="breadcrumb-item active" data-id="DetalleAPP"><span>Comunicaciones<span></span></span></li><li class="breadcrumb-item refresh"><a href="#" id="recargarDetalleAPP"><i class="fa fa-refresh" aria-hidden="true"></i></a></li></ol>
        </div>
        <div class="col-sm-12 col-md-4" id="msgGestion">
        </div>
    </div>
</div>
<div class="container-fluid oculto" id="containerTableroAPP">
    <div class="card">
        <div class="card-body">

            <h6 class="card-title mb-2 text-muted">Mis Asignadas</h6>
            <div class="row mb-2" id="rowTableroAPP"><div class="col-md-6">
    <div class="card">
        <div class="card-body">
            <h6 class="card-title mb-2 text-muted font-weight-bold"><span class="tablero-titulo">Comunicaciones</span><span class="badge badge-primary float-right"><a class="ma-gestionar ma-gestionar-t">20</a></span></h6>
            <div class="row">
                <div class="col-lg-4 col-md-12"><div class="chartjs-size-monitor"><div class="chartjs-size-monitor-expand"><div class=""></div></div><div class="chartjs-size-monitor-shrink"><div class=""></div></div></div>
                    <canvas class="pie-oportunidad-abiertas chartjs-render-monitor" width="308" height="308" id="pieOportunidadAbiertas1" style="display: block; width: 308px; height: 308px; cursor: default;"></canvas>
                </div>
                <div class="col-lg-8 col-md-12"><div class="chartjs-size-monitor"><div class="chartjs-size-monitor-expand"><div class=""></div></div><div class="chartjs-size-monitor-shrink"><div class=""></div></div></div>
                    <canvas class="bar-secuencia-abiertas chartjs-render-monitor" max-width="100" max-height="100" id="barSecuenciaAbiertas1" width="308" height="154" style="display: block; width: 308px; height: 154px; cursor: default;"></canvas>
                </div>
            </div>
            <hr class="mb-2">
            <div class="row tablero-alertas">
            </div>
        </div>
    </div>
</div></div>
        </div>
    </div>
    <div class="alert alert-warning oculto" role="alert" id="divDocsPF">
        <h5 class="alert-heading link"> <span class="fa-stack fa-lg"> <i class="fa fa-file-o fa-stack-2x"></i><i class="fa fa-exclamation-triangle fa-stack-1x"></i></span><span id="docsPF"></span> documentos pendientes por firma digital</h5>
        <p>Son documentos previamente radicados a los cuales no les fue aplicada la firma digital</p>
    </div>
</div>

<div class="col-sm-3 oculto" id="tableroNegocio">
    <div class="card">
        <div class="card-body">
            <div class="row" style="min-height:55px;">
                <div class="col-10">
                    <small class="tablero-titulo font-weight-bold"></small>
                </div>
                <div class="col-2">
                    <span class="badge badge-primary float-right"><a class="ma-gestionar ma-gestionar-t"></a></span>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-8 col-md-12">
                    <canvas class="bar-negocio-abiertas" max-width="100" max-height="100"></canvas>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="col-md-6 oculto" id="tableroAPP">
    <div class="card">
        <div class="card-body">
            <h6 class="card-title mb-2 text-muted font-weight-bold"><span class="tablero-titulo"></span><span class="badge badge-primary float-right"><a class="ma-gestionar ma-gestionar-t"></a></span></h6>
            <div class="row">
                <div class="col-lg-4 col-md-12">
                    <canvas class="pie-oportunidad-abiertas" width="200" height="200"></canvas>
                </div>
                <div class="col-lg-8 col-md-12">
                    <canvas class="bar-secuencia-abiertas" max-width="100" max-height="100"></canvas>
                </div>
            </div>
            <hr class="mb-2">
            <div class="row tablero-alertas">
            </div>
        </div>
    </div>
</div>

<div class="container-fluid" id="containerDetalleAPP">
    <div class="card">
        <div class="card-body">
            <h6 class="card-title mb-2 text-muted">Tablero mis asignadas <div class="toggle btn btn-xs btn-outline-info" data-toggle="toggle" style="width: 150px; height: 0px;"><input id="toggle-modovista" type="checkbox" checked=""><div class="toggle-group"><label class="btn btn-outline-info btn-xs toggle-on">Por secuencia</label><label class="btn btn-outline-info btn-xs toggle-off">Por tipo de tarea</label><span class="toggle-handle btn btn-light btn-xs"></span></div></div> <span class="colapsar" data-toggle="collapse" href="#collapseDetalleAPP" role="button"></span></h6>
            <div id="collapseDetalleAPP" class="collapse show">
                <div class="row mb-2 align-items-center">
                    <div class="col-md-7 pr-0 pl-2" id="resumenDetalleAPP">
                        <div class="row" id="secuenciaEtapas">
                            <div class="col-md-12">
                                <div class="cd-breadcrumb-body">
                                    <section>
                                        <nav>
                                            <ol class="cd-breadcrumb triangle"><li id="0"><a style="cursor:pointer;" data-id="0" data-total="20" data-titulo="Todas">Todas <span class="badge badge-secondary text-light">20</span></a></li><li id="1" class="current"><a style="cursor:pointer;" data-id="1" data-total="20" data-titulo="Gestionar">Gestionar <span class="badge badge-secondary text-light">20</span></a></li><li id="2"><a style="" data-id="2" data-total="0" data-titulo="Revisar respuesta">Revisar respuesta <span class="badge badge-secondary text-light">0</span></a></li><li id="3"><a style="" data-id="3" data-total="0" data-titulo="Aprobar respuesta">Aprobar respuesta <span class="badge badge-secondary text-light">0</span></a></li><li id="30"><a style="" data-id="30" data-total="0" data-titulo="Revisar/Aprobar documento">Revisar/Aprobar documento <span class="badge badge-secondary text-light">0</span></a></li></ol>
                                        </nav>
                                    </section>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-5">
                        <div class="card">
                            <div class="card-body">
                                <ul class="list-group list-group-flush resumen-ma-con-tareas" id="resumenDetalleAPPConTareas"><b>Novedades de mis asignadas con: </b><li class="list-group-item"><div class="row align-items-center"><div class="col-md-12 col-lg-6">"Tareas Relacionadas" <b>pendientes</b></div><div class="col"><a class="ma-gestionar ma-gestionar-v ma-medio" data-clase="1" data-oportunidad="1" data-c="4" data-titulo="&quot;Tareas Relacionadas&quot; &lt;b&gt;pendientes&lt;/b&gt;">4</a></div><div class="col"><a class="ma-gestionar ma-gestionar-a ma-medio" data-clase="1" data-oportunidad="2" data-c="0" data-titulo="&quot;Tareas Relacionadas&quot; &lt;b&gt;pendientes&lt;/b&gt;">0</a></div><div class="col"><a class="ma-gestionar ma-gestionar-r ma-medio" data-clase="1" data-oportunidad="3" data-c="0" data-titulo="&quot;Tareas Relacionadas&quot; &lt;b&gt;pendientes&lt;/b&gt;">0</a></div></div></li><li class="list-group-item"><div class="row align-items-center"><div class="col-md-12 col-lg-6">"Tareas Relacionadas" <b>cerradas</b></div><div class="col"><a class="ma-gestionar ma-gestionar-v ma-medio" data-clase="2" data-oportunidad="1" data-c="1" data-titulo="&quot;Tareas Relacionadas&quot; &lt;b&gt;cerradas&lt;/b&gt;">1</a></div><div class="col"><a class="ma-gestionar ma-gestionar-a ma-medio" data-clase="2" data-oportunidad="2" data-c="0" data-titulo="&quot;Tareas Relacionadas&quot; &lt;b&gt;cerradas&lt;/b&gt;">0</a></div><div class="col"><a class="ma-gestionar ma-gestionar-r ma-medio" data-clase="2" data-oportunidad="3" data-c="0" data-titulo="&quot;Tareas Relacionadas&quot; &lt;b&gt;cerradas&lt;/b&gt;">0</a></div></div></li><li class="list-group-item"><div class="row align-items-center"><div class="col-md-12 col-lg-6">"Ciclos de aprobación" <b>pendientes</b></div><div class="col"><a class="ma-gestionar ma-gestionar-v ma-medio" data-clase="7" data-oportunidad="1" data-c="3" data-titulo="&quot;Ciclos de aprobación&quot; &lt;b&gt;pendientes&lt;/b&gt;">3</a></div><div class="col"><a class="ma-gestionar ma-gestionar-a ma-medio" data-clase="7" data-oportunidad="2" data-c="0" data-titulo="&quot;Ciclos de aprobación&quot; &lt;b&gt;pendientes&lt;/b&gt;">0</a></div><div class="col"><a class="ma-gestionar ma-gestionar-r ma-medio" data-clase="7" data-oportunidad="3" data-c="0" data-titulo="&quot;Ciclos de aprobación&quot; &lt;b&gt;pendientes&lt;/b&gt;">0</a></div></div></li></ul>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row mb-2 align-items-start oculto" id="resumenDetalleAPPXTipificacion">
                </div>
            </div>
        </div>
    </div>
    <!--	<div class="card" id="cardTareas">
            <div class="card-body">
                <h6 class="card-title mb-2 text-muted"><span class="card-titulo"></span> <span class="colapsar" data-toggle="collapse" href="#collapseTareas" role="button"></span></h6>
                <div id="collapseTareas" class="collapse show">
                    -->
    <div class="row">
        <div class="col-12"><h6 id="tituloTabla"></h6></div>
        <div class="col-12" id="gestionarTabla"><div class="row mb-1"><div class="col-sm-12 oculto" id="divBotonesMasivo"><button class="btn btn-outline-info btn-masivo" id="btnReasignar" data-toggle="modal" data-target="#modalGestionarTabla" data-backdrop="static" data-keyboard="false" data-tipo="reasignar" data-titulo="Reasignar">Reasignar masivo</button>&nbsp; <button class="btn btn-outline-info btn-masivo" id="btnCerrar" data-toggle="modal" data-target="#modalGestionarTabla" data-backdrop="static" data-keyboard="false" data-tipo="cerrar" data-titulo="Cerrar">Cerrar masivo</button></div></div> <div id="tblGestionar_wrapper" class="dataTables_wrapper container-fluid dt-bootstrap4 no-footer"><div class="row"><div class="col-sm-12 col-md-3"><div class="dataTables_length" id="tblGestionar_length"><label>Mostrar <select name="tblGestionar_length" aria-controls="tblGestionar" class="form-control form-control-sm"><option value="10">10</option><option value="25">25</option><option value="50">50</option><option value="100">100</option></select> registros</label></div></div><div class="col-sm-12 col-md-3"><div id="tblGestionar_filter" class="dataTables_filter"><label>Buscar:<input type="search" class="form-control form-control-sm" placeholder="" aria-controls="tblGestionar" data-toggle="tooltip" data-placement="top" title="" data-original-title="mínimo 3 caracteres"></label></div></div><div class="col-sm-12 col-md-6"><div class="div-semaforo"><button id="todas" type="button" class="btn" data-tipo="0"><span class="badge badge-secondary text-light">3</span> Nuevas</button><button id="todas" type="button" class="btn" data-tipo="1"><span class="badge badge-success text-light">19</span> A tiempo</button><button id="todas" type="button" class="btn" data-tipo="2"><span class="badge badge-warning text-light">0</span> Por vencer</button><button id="todas" type="button" class="btn" data-tipo="3"><span class="badge badge-danger text-light">0</span> Vencidas</button></div></div></div><div class="row"><div class="col-sm-12"><table class="table table-striped table-bordered dataTable no-footer dtr-inline collapsed" cellspacing="0" id="tblGestionar" width="100%" role="grid" aria-describedby="tblGestionar_info" style="width: 100%;"><thead><tr role="row"><th class="control sorting_disabled" rowspan="1" colspan="1" style="width: 18px;" aria-label=""></th><th class="sorting_disabled" rowspan="1" colspan="1" style="width: 13px;" aria-label=""><input type="checkbox" name="selectAll" id="selectAll"></th><th class="dt-110 sorting_desc" tabindex="0" aria-controls="tblGestionar" rowspan="1" colspan="1" style="width: 118px;" aria-sort="descending" aria-label="Nro. Radicación: Activar para ordenar la columna de manera ascendente">Nro. Radicación</th><th class="dt-120 sorting" tabindex="0" aria-controls="tblGestionar" rowspan="1" colspan="1" style="width: 210px;" aria-label="Proceso / Tarea: Activar para ordenar la columna de manera ascendente">Proceso / Tarea</th><th class="dt-110 sorting" tabindex="0" aria-controls="tblGestionar" rowspan="1" colspan="1" style="width: 119px;" aria-label="Vencimiento proceso / Tarea: Activar para ordenar la columna de manera ascendente">Vencimiento proceso / Tarea</th><th id="etiquetaCliente" class="dt-170 sorting" tabindex="0" aria-controls="tblGestionar" rowspan="1" colspan="1" style="width: 0px; display: none;" aria-label="Remitente: Activar para ordenar la columna de manera ascendente">Remitente</th><th class="dt-250 sorting" tabindex="0" aria-controls="tblGestionar" rowspan="1" colspan="1" style="width: 0px; display: none;" aria-label="Descripción: Activar para ordenar la columna de manera ascendente">Descripción</th><th class="dt-120 sorting" tabindex="0" aria-controls="tblGestionar" rowspan="1" colspan="1" style="width: 0px; display: none;" aria-label="Fecha radicación: Activar para ordenar la columna de manera ascendente">Fecha radicación</th><th class="dt-350 sorting_disabled" rowspan="1" colspan="1" style="width: 0px; display: none;" aria-label="Información adicional">Información adicional</th></tr></thead><tbody><tr role="row" class="odd"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0427453.2" id="chkSol2026-ER-0427453.2" value="2026-ER-0427453.2" data-idsol="2026-ER-0427453.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0427453</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - IMPUGNACION DE FALLO DE TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">ASIGNADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">28 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 0 de 3, faltan 3</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">28 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 0 de 3, faltan 3</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>TRIBUNAL SUPERIOR DEL DISTRITO JUDICIAL DE POPAYÁN</p><p><i class="fa fa-envelope"></i>sacftribsupayan@cendoj.ramajudicial.gov.co</p><p><i class="fa fa-home"></i>Popayán - Cauca</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>JAIME LEONARDO CHAPARRO PERALTA</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para tramite, gracias (BOT 3)</p><hr class="mb-1 mt-1"><p>Oficio No. STSP-6548-6551</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Proceso judicial Nro.: </b><span> 19698310400220261011601</span></p><p><b>Despacho judicial: </b><span> JUZGADO 002 PENAL DEL CIRCUITO DE SANTANDER DE QUILICHAO</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">23 de septiembre de 2026</p><p class="mb-0">02:27:17 pm</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>ASIGNADO</td></tr><tr><td><b>Último evento:</b></td><td>23 de septiembre de 2026 02:27:17 pm<br>ANDREA MARCELA MEJÍA VELANDIA<br>Solicitud creada en fecha: 23 de septiembre de 2026 3:29:28 p.&nbsp;m..<br> Asignación de la solicitud a DIANA CAMILA ZAPATA VALENCIA.</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="even"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0426680.2" id="chkSol2026-ER-0426680.2" value="2026-ER-0426680.2" data-idsol="2026-ER-0426680.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0426680</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - NOTIFICACION DE ACCION DE TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">ASIGNADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">28 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 0 de 3, faltan 3</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">28 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 0 de 3, faltan 3</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>JUZGADO SEGUNDO PROMISCUO MUNICIPAL DE PLATO</p><p><i class="fa fa-envelope"></i>j02pmpalplato@cendoj.ramajudicial.gov.co</p><p><i class="fa fa-home"></i>Plato - Magdalena</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>CARLOS ARTURO GARCÍA GUERRERO</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para tramite, gracias.</p><hr class="mb-1 mt-1"><p>Escrito de Tutela, Auto Admision y Oficio de Notificacion 2026-00500</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Proceso judicial Nro.: </b><span> 47555408900220260050000</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">23 de septiembre de 2026</p><p class="mb-0">10:20:07 am</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>ASIGNADO</td></tr><tr><td><b>Último evento:</b></td><td>23 de septiembre de 2026 10:20:07 am<br>ANDREA MARCELA MEJÍA VELANDIA<br>Solicitud creada en fecha: 23 de septiembre de 2026 3:51:05 p.&nbsp;m..<br> Asignación de la solicitud a DIANA CAMILA ZAPATA VALENCIA.</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="odd"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0426332.2" id="chkSol2026-ER-0426332.2" value="2026-ER-0426332.2" data-idsol="2026-ER-0426332.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0426332</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - NOTIFICACION DE ACCION DE TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">ASIGNADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">28 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 0 de 3, faltan 3</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">28 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 0 de 3, faltan 3</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>JUZGADO TREINTA Y SEIS CIVIL DEL CIRCUITO DE BOGOTÁ</p><p><i class="fa fa-envelope"></i>ccto36bt@cendoj.ramajudicial.gov.co</p><p><i class="fa fa-home"></i>Bogotá, D.C. - Bogotá, D.C.</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>ELISA ANDREA ORDUZ BARRETO</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para tramite, gracias.</p><hr class="mb-1 mt-1"><p>[!]ADMISION TUTELA 2026-00578</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Proceso judicial Nro.: </b><span> 11001310303620260057800</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">23 de septiembre de 2026</p><p class="mb-0">08:46:16 am</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>ASIGNADO</td></tr><tr><td><b>Último evento:</b></td><td>23 de septiembre de 2026 08:46:16 am<br>ANDREA MARCELA MEJÍA VELANDIA<br>Solicitud creada en fecha: 23 de septiembre de 2026 3:42:55 p.&nbsp;m..<br> Asignación de la solicitud a DIANA CAMILA ZAPATA VALENCIA.</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="even"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0425458.2" id="chkSol2026-ER-0425458.2" value="2026-ER-0425458.2" data-idsol="2026-ER-0425458.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0425458</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - NOTIFICACION DE ACCION DE TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">NOTIFICADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">25 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">25 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>TRIBUNAL ADMINISTRATIVO DE BOYACÁ</p><p><i class="fa fa-envelope"></i>sectradmboy@cendoj.ramajudicial.gov.co</p><p><i class="fa fa-home"></i>Tunja - Boyacá</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>ADRIANA DEL PILAR CAMACHO RUIDIAZ</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para tramite, gracias.</p><hr class="mb-1 mt-1"><p>NOTIFICA ACTUACION PROCESAL RAD 2026-00160-01</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Proceso judicial Nro.: </b><span> 15001333300520260016001</span></p><p><b>Despacho judicial: </b><span> JUZGADO 005 ADMINISTRATIVO DE TUNJA</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">22 de septiembre de 2026</p><p class="mb-0">05:05:16 pm</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>NOTIFICADO</td></tr><tr><td><b>Último evento:</b></td><td>23 de septiembre de 2026 11:54:31 am<br>DIANA CAMILA ZAPATA VALENCIA<br>Cambio de estado a NOTIFICADO</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="odd"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0425450.2" id="chkSol2026-ER-0425450.2" value="2026-ER-0425450.2" data-idsol="2026-ER-0425450.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0425450</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div><hr class="mb-1 mt-1"><p class="mb-0"><small><b>1 doc con ciclo</b></small></p><ul><li><small> 1 por aprobar</small></li></ul></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - NOTIFICACION DE ACCION DE TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">NOTIFICADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">25 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">25 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>JUZGADO PRIMERO CIVIL MUNICIPAL</p><p><i class="fa fa-envelope"></i>j01cmcartago@cendoj.ramajudicial.gov.co</p><p><i class="fa fa-home"></i>Guadalajara De Buga - Valle Del Cauca</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>ADRIANA LÓPEZ LEÓN</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para tramite, gracias.</p><hr class="mb-1 mt-1"><p>2026-00629 ADMITE TUTELA SECRETARÍA DE EDUCACIÓN DEL VALLE DEL CAUCA</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Proceso judicial Nro.: </b><span> 76147400300120260062900</span></p><p><b>Despacho judicial: </b><span> JUZGADO 001 CIVIL MUNICIPAL DE CARTAGO</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">22 de septiembre de 2026</p><p class="mb-0">05:03:59 pm</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>NOTIFICADO</td></tr><tr><td><b>Último evento:</b></td><td>23 de septiembre de 2026 10:29:41 am<br>DIANA CAMILA ZAPATA VALENCIA<br>Cambio de estado a NOTIFICADO</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="even"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0425297.2" id="chkSol2026-ER-0425297.2" value="2026-ER-0425297.2" data-idsol="2026-ER-0425297.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0425297</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - NOTIFICACION DE ACCION DE TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">NOTIFICADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">25 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">25 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>JUZGADO 39 CIVIL DEL CIRCUITO DE BOGOTA</p><p><i class="fa fa-phone"></i>3532666-71339</p><p><i class="fa fa-envelope"></i>ccto39bt@cendoj.ramajudicial.gov.co</p><p><i class="fa fa-home"></i>Cr 10 # 14 33</p><p><i class="fa fa-home"></i>Bogotá, D.C. - Bogotá, D.C.</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>Mauricio De Los Reyes Cabeza Cabeza</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para tramite, gracias.</p><hr class="mb-1 mt-1"><p>Notificación admisión tutela 11001310303920260054000</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Proceso judicial Nro.: </b><span> 11001310303920260054000</span></p><p><b>Despacho judicial: </b><span> JUZGADO 039 CIVIL DEL CIRCUITO DE BOGOTÁ</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">22 de septiembre de 2026</p><p class="mb-0">04:25:31 pm</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>NOTIFICADO</td></tr><tr><td><b>Último evento:</b></td><td>23 de septiembre de 2026 10:14:56 am<br>DIANA CAMILA ZAPATA VALENCIA<br>Cambio de estado a NOTIFICADO</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="odd"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0425296.2" id="chkSol2026-ER-0425296.2" value="2026-ER-0425296.2" data-idsol="2026-ER-0425296.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0425296</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div><hr class="mb-1 mt-1"><p class="mb-0"><small><b>1 doc con ciclo</b></small></p><ul><li><small> 1 por aprobar</small></li></ul></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - NOTIFICACION DE ACCION DE TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">NOTIFICADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">25 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">25 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>JUZGADO TERCERO ADMINISTRATIVO DE SANTA MARTA</p><p><i class="fa fa-envelope"></i>j03admsmta@cendoj.ramajudicial.gov.co</p><p><i class="fa fa-home"></i>Santa Marta - Magdalena</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>PEDRO ANTONIO VASQUEZ GALVIS</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para tramite, gracias.</p><hr class="mb-1 mt-1"><p>Notificacion admite    ACTOR KELLY JOHANNA MARTINEZ VILARETE DEMANDADO FONDO NACIONAL DE PRESTACIONES SOCIALES DEL MAGISTERIO (FOMAG) Y FIDUCIARIA LA-(FIDUPREVISORA) RADICACIÓN 47-001-3333-003-2026-00245-00</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Proceso judicial Nro.: </b><span> 47001333300320250028300</span></p><p><b>Despacho judicial: </b><span> JUZGADO 003 ADMINISTRATIVO DE SANTA MARTA</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">22 de septiembre de 2026</p><p class="mb-0">04:25:03 pm</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>NOTIFICADO</td></tr><tr><td><b>Último evento:</b></td><td>23 de septiembre de 2026 09:49:14 am<br>DIANA CAMILA ZAPATA VALENCIA<br>Cambio de estado a NOTIFICADO</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="even"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0425293.2" id="chkSol2026-ER-0425293.2" value="2026-ER-0425293.2" data-idsol="2026-ER-0425293.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0425293</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - NOTIFICACION DE ACCION DE TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">NOTIFICADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">25 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">25 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>Secretaría Sala Penal Tribunal Superior - N. De Santander - Cúcuta</p><p><i class="fa fa-envelope"></i>secsptsupcuc@notificacionesrj.gov.co</p><p><i class="fa fa-home"></i>San José De Cúcuta - Norte De Santander</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>EDGAR MANUEL CAICEDO BARRERA</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para tramite, gracias.</p><hr class="mb-1 mt-1"><p>AUTO DECRETA NULIDAD RAD. 2026-00182-01 CARLOS ANDRÉS ARENGAS ALVERNIA</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Proceso judicial Nro.: </b><span> 54498310300120260018201</span></p><p><b>Despacho judicial: </b><span> JUZGADO 001 CIVIL DEL CIRCUITO DE OCAÑA</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">22 de septiembre de 2026</p><p class="mb-0">04:24:39 pm</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>NOTIFICADO</td></tr><tr><td><b>Último evento:</b></td><td>23 de septiembre de 2026 09:36:05 am<br>DIANA CAMILA ZAPATA VALENCIA<br>Cambio de estado a NOTIFICADO</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="odd"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0425156.2" id="chkSol2026-ER-0425156.2" value="2026-ER-0425156.2" data-idsol="2026-ER-0425156.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0425156</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div><hr class="mb-1 mt-1"><p class="mb-0"><small><b>1 doc con ciclo</b></small></p><ul><li><small> 1 por aprobar</small></li></ul></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - NOTIFICACION DE ACCION DE TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">NOTIFICADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">25 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">25 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>JUZGADO SEGUNDO LABORAL MUNICIPAL DE CÚCUTA</p><p><i class="fa fa-envelope"></i>j02mpclcuc@cendoj.ramajudicial.gov.co</p><p><i class="fa fa-home"></i>Avenida 4E No 7 10a Barrio Popular Edificio Temis Oficina 105</p><p><i class="fa fa-home"></i>San José De Cúcuta - Norte De Santander</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>ÁLVARO ENRIQUE BUENDÍA ROA</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para tramite, gracias.</p><hr class="mb-1 mt-1"><p>NOTIFICACION AUTO ADMITE TUTELA 2026-10577</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Proceso judicial Nro.: </b><span> 54001400300220261057700</span></p><p><b>Despacho judicial: </b><span> JUZGADO 002 CIVIL MUNICIPAL DE CÚCUTA</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">22 de septiembre de 2026</p><p class="mb-0">03:46:52 pm</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>NOTIFICADO</td></tr><tr><td><b>Último evento:</b></td><td>23 de septiembre de 2026 07:06:54 am<br>DIANA CAMILA ZAPATA VALENCIA<br>Cambio de estado a NOTIFICADO</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="even"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0424985.2" id="chkSol2026-ER-0424985.2" value="2026-ER-0424985.2" data-idsol="2026-ER-0424985.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0424985</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div><hr class="mb-1 mt-1"><p class="mb-1"><small> 1 "Tareas relacionadas" pendientes de 2</small></p></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - NOTIFICACION DE ACCION DE TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">NOTIFICADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">25 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">25 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>JUZGADO PROMISCUO MUNICIPAL DE COGUA</p><p><i class="fa fa-phone"></i>3154550695</p><p><i class="fa fa-envelope"></i>jprmpalcogua@cendoj.ramajudicial.gov.co</p><p><i class="fa fa-home"></i>Calle 4 No 4 37 Piso 2 Cogua</p><p><i class="fa fa-home"></i>Cogua - Cundinamarca</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>MIGUEL ANGEL RIAÑO NIÑO</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para tramite, gracias.</p><hr class="mb-1 mt-1"><p>RV: Notificación Oficio No. 1395 dentro de la Acción de Tutela 2026-00366</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Proceso judicial Nro.: </b><span> 25200408900120260036600</span></p><p><b>Despacho judicial: </b><span> JUZGADO 001 PROMISCUO MUNICIPAL DE COGUA</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">22 de septiembre de 2026</p><p class="mb-0">03:11:02 pm</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>NOTIFICADO</td></tr><tr><td><b>Último evento:</b></td><td>22 de septiembre de 2026 08:41:06 pm<br>DIANA CAMILA ZAPATA VALENCIA<br>Cambio de estado a NOTIFICADO</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="odd"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0424833.2" id="chkSol2026-ER-0424833.2" value="2026-ER-0424833.2" data-idsol="2026-ER-0424833.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0424833</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - NOTIFICACION DE ACCION DE TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">NOTIFICADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">25 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">25 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>JUZGADO 25 DE FAMILIA DEL CIRCUITO DE BOGOTÁ</p><p><i class="fa fa-envelope"></i>flia25bt@cendoj.ramajudicial.gov.co</p><p><i class="fa fa-home"></i>CLL 12C No 7-36 Edificio NEMQUETEBA Piso 17</p><p><i class="fa fa-home"></i>Bogotá, D.C. - Bogotá, D.C.</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>Deyvid F Larrota C</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para tramite, gracias.</p><hr class="mb-1 mt-1"><p>NOTIFICACION DE LA SENTENCIA DE LA ACCIÓN DE TUTELA 2026-00695-00</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Proceso judicial Nro.: </b><span> 11001311002520260069500</span></p><p><b>Despacho judicial: </b><span> JUZGADO 025 DE FAMILIA DE BOGOTÁ</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">22 de septiembre de 2026</p><p class="mb-0">02:38:56 pm</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>NOTIFICADO</td></tr><tr><td><b>Último evento:</b></td><td>22 de septiembre de 2026 08:21:29 pm<br>DIANA CAMILA ZAPATA VALENCIA<br>Cambio de estado a NOTIFICADO</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="even"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0424194.2" id="chkSol2026-ER-0424194.2" value="2026-ER-0424194.2" data-idsol="2026-ER-0424194.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0424194</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - PROCESO SIN RADICADO TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">NOTIFICADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">25 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">25 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 1 de 3, faltan 2</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>JUZGADO QUINTO ADMINISTRATIVO SANTA MARTA</p><p><i class="fa fa-envelope"></i>jadmin05smr@notificacionesrj.gov.co</p><p><i class="fa fa-home"></i>Santa Marta - Magdalena</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>Rocío Esther Nieto Salebe</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para tramite, gracias.</p><hr class="mb-1 mt-1"><p>SE NOTIFICA ADMISION ACCIÓN DE TUTELA DE ROCIO NIETO SALEBE CONTRA JUZGADO QUINTO ADMIN DE STA MTA DEMANDA</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Entidad de control:</b> Juzgado 05 Administrativo - Magdalena</p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">22 de septiembre de 2026</p><p class="mb-0">10:45:20 am</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>NOTIFICADO</td></tr><tr><td><b>Último evento:</b></td><td>22 de septiembre de 2026 08:02:09 pm<br>DIANA CAMILA ZAPATA VALENCIA<br>Cambio de estado a NOTIFICADO</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="odd"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0423231.2" id="chkSol2026-ER-0423231.2" value="2026-ER-0423231.2" data-idsol="2026-ER-0423231.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0423231</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - NOTIFICACION DE ACCION DE TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">NOTIFICADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">24 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 2 de 3, faltan 1</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">24 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 2 de 3, faltan 1</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>INICIATIVA LEGAL</p><p><i class="fa fa-envelope"></i>Info.iniciativalegal@gmail.com</p><p><i class="fa fa-home"></i>Medellín - Antioquia</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>CAMILO MONTOYA DUQUE</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Cierre, proviene de externos</p><hr class="mb-1 mt-1"><p>Re: NOTIFICACIÓN ADMITE TUTELA RAD.&nbsp; 05-001 31 05-013-2026-10194-00</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Proceso judicial Nro.: </b><span> 05001408801620260025001</span></p><p><b>Despacho judicial: </b><span> JUZGADO 016 PENAL MUNICIPAL CON FUNCIÓN DE CONTROL DE GARANTÍAS DE MEDELLÍN</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">21 de septiembre de 2026</p><p class="mb-0">06:01:37 pm</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>NOTIFICADO</td></tr><tr><td><b>Último evento:</b></td><td>22 de septiembre de 2026 10:46:26 am<br>DIANA CAMILA ZAPATA VALENCIA<br>Cambio de estado a NOTIFICADO</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="even"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0423203.2" id="chkSol2026-ER-0423203.2" value="2026-ER-0423203.2" data-idsol="2026-ER-0423203.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0423203</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div><hr class="mb-1 mt-1"><p class="mb-1"><small> 1 "Tareas relacionadas" pendientes de 2</small></p></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - NOTIFICACION DE ACCION DE TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">NOTIFICADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">24 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 2 de 3, faltan 1</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">24 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 2 de 3, faltan 1</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>JUZGADO 11 ADMINISTRATIVO DE BOGOTA</p><p><i class="fa fa-envelope"></i>admin11bt@cendoj.ramajudicial.gov.co</p><p><i class="fa fa-home"></i>Bogotá, D.C. - Bogotá, D.C.</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>ANDREA SANABRIA ESPINOSA</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para tramite, gracias.</p><hr class="mb-1 mt-1"><p>NOTIFICA ACTUACION PROCESAL RAD 2026-00402-00</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Proceso judicial Nro.: </b><span> 11001333501120260040200</span></p><p><b>Despacho judicial: </b><span> JUZGADO 011 ADMINISTRATIVO DE LA SECCIÓN SEGUNDA DE BOGOTÁ</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">21 de septiembre de 2026</p><p class="mb-0">05:54:14 pm</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>NOTIFICADO</td></tr><tr><td><b>Último evento:</b></td><td>22 de septiembre de 2026 07:57:27 pm<br>DIANA CAMILA ZAPATA VALENCIA<br>Cambio de estado a NOTIFICADO</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="odd"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0422992.2" id="chkSol2026-ER-0422992.2" value="2026-ER-0422992.2" data-idsol="2026-ER-0422992.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0422992</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - NOTIFICACION DE ACCION DE TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">NOTIFICADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">24 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 2 de 3, faltan 1</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">24 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 2 de 3, faltan 1</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>Corporación Iberoamericana de Educación para el Trabajo y el Desarrollo Humano.</p><p><i class="fa fa-envelope"></i>director@cipet.edu.co</p><p><i class="fa fa-home"></i>Floridablanca - Santander</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>William Andrés García Cifuentes</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Cierre, proviene de externos</p><hr class="mb-1 mt-1"><p>CONTESTACIÓN ACCIÓN DE TUTELA – RAD. 76001-40-71-001-2026-00347-00 – JAZMÍN TATIANA SALINAS ZAPATA vs. CIPET – AUTO No. 1046</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Proceso judicial Nro.: </b><span> 76001407100120260034700</span></p><p><b>Despacho judicial: </b><span> JUZGADO 001 PENAL MUNICIPAL PARA ADOLESCENTES CON FUNCIÓN DE CONTROL DE GARANTÍAS DE CALI</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">21 de septiembre de 2026</p><p class="mb-0">04:46:12 pm</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>NOTIFICADO</td></tr><tr><td><b>Último evento:</b></td><td>22 de septiembre de 2026 05:14:43 pm<br>DIANA CAMILA ZAPATA VALENCIA<br>Cambio de estado a NOTIFICADO</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="even"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0421852.2" id="chkSol2026-ER-0421852.2" value="2026-ER-0421852.2" data-idsol="2026-ER-0421852.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0421852</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div><hr class="mb-1 mt-1"><p class="mb-1"><small> 0 "Tareas relacionadas" pendientes de 3</small></p></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - PROCESO SIN RADICADO TUTELA</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">NOTIFICADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">24 de septiembre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 2 de 3, faltan 1</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">24 de septiembre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 2 de 3, faltan 1</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>CORTE CONSTITUCIONAL</p><p><i class="fa fa-envelope"></i>salasrevisionA@corteconstitucional.gov.co</p><p><i class="fa fa-home"></i>Bogotá, D.C. - Bogotá, D.C.</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>Sterly Alvarado Cano</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para tramite, gracias.</p><hr class="mb-1 mt-1"><p>T-12046262 OFICIO OPT-A-487-2026 AUTO DE PRUEBAS 18-Sep-26</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Entidad de control:</b> CORTE CONSTITUCIONAL</p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">21 de septiembre de 2026</p><p class="mb-0">11:07:51 am</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>NOTIFICADO</td></tr><tr><td><b>Último evento:</b></td><td>21 de septiembre de 2026 04:14:17 pm<br>DIANA CAMILA ZAPATA VALENCIA<br>Cambio de estado a NOTIFICADO</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="odd"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0414985.2" id="chkSol2026-ER-0414985.2" value="2026-ER-0414985.2" data-idsol="2026-ER-0414985.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0414985</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - CITACION A CONSEJOS, JUNTAS, DIRECTIVAS Y DELEGACIONES (UNIV.NACIONAL, CONSEJO ASESOR CIENCIA Y TECN</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">NOTIFICADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">7 de octubre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 5 de 15, faltan 10</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">7 de octubre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 5 de 15, faltan 10</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>Maria Paula Perilla Rojas</p><p><i class="fa fa-barcode"></i>CC - 0000</p><p><i class="fa fa-envelope"></i>maria.perilla@mininterior.gov.co</p><p><i class="fa fa-home"></i>Bogotá, D.C. - Bogotá, D.C.</p></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para revisión Sec Priv</p><hr class="mb-1 mt-1"><p>Convocatoria – Jornadas de Pre-SNARIV y Protocolización de Planes Específicos 2026</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> INVITACIONES</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">16 de septiembre de 2026</p><p class="mb-0">11:21:41 am</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>NOTIFICADO</td></tr><tr><td><b>Último evento:</b></td><td>21 de septiembre de 2026 10:53:41 am<br>DIANA CAMILA ZAPATA VALENCIA<br>Cambio de estado a NOTIFICADO</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="even"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0414786.2" id="chkSol2026-ER-0414786.2" value="2026-ER-0414786.2" data-idsol="2026-ER-0414786.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0414786</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div><hr class="mb-1 mt-1"><p class="mb-1"><small> 1 "Tareas relacionadas" pendientes de 2</small></p></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - SOLICITUDES ENTES GUBERNAMENTALES</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">NOTIFICADO</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">7 de octubre de 2026</p><p class="mb-0 font-weight-bold">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 5 de 15, faltan 10</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">7 de octubre de 2026</p><p class="mb-0">11:59:58 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 5 de 15, faltan 10</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>MINISTERIO DEL INTERIOR</p><p><i class="fa fa-phone"></i>6012427400</p><p><i class="fa fa-envelope"></i>gabriela.araque@mininterior.gov.co</p><p><i class="fa fa-home"></i>Cra 8 No 12B -3</p><p><i class="fa fa-home"></i>Bogotá, D.C. - Bogotá, D.C.</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>GABRIELA ARAQUE GARCÍA</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para revisión Sec Priv</p><hr class="mb-1 mt-1"><p>Solicitud de información y Remisión de formatos para la consolidación del informe de cumplimiento – Sentencia T-420 de 2025</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> DERECHO DE PETICIÓN</span></p><p><b>Casos asociados: </b><span>2026-ER-0408356</span></p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">16 de septiembre de 2026</p><p class="mb-0">10:08:44 am</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>NOTIFICADO</td></tr><tr><td><b>Último evento:</b></td><td>21 de septiembre de 2026 08:24:34 am<br>DIANA CAMILA ZAPATA VALENCIA<br>Cambio de estado a NOTIFICADO</td></tr><tr></tr></tbody></table></td></tr><tr role="row" class="odd"><td class=" control" tabindex="0"></td><td><input type="checkbox" name="chkSol2026-ER-0410807.2" id="chkSol2026-ER-0410807.2" value="2026-ER-0410807.2" data-idsol="2026-ER-0410807.2"></td><td class="dt-110 sorting_1"><p>2026-ER-0410807</p><div class="btn-group mb-2" role="group"><button type="button" class="btn btn-success btn-sm gestion"><i class="fa fa-cog" aria-hidden="true"></i></button></div><hr class="mb-1 mt-1"><p class="mb-1"><small> 3 "Tareas relacionadas" pendientes de 3</small></p><hr class="mb-1 mt-1"><p class="mb-1"><small> Tarea "Reprogramada"</small></p></td><td class=" dt-120"><p class="mb-1">Comunicaciones Recibidas - FALLO DE TUTELA (15 DÍAS)</p><hr class="mb-1 mt-1"><p class="mb-1">Gestión o Respuesta a Documento</p><hr class="mb-1 mt-1"><p class="mb-1">Cambio Fecha Vencimiento</p></td><td class=" dt-110"><p class="mb-1"></p><p class="mb-0 font-weight-bold">5 de octubre de 2026</p><p class="mb-0 font-weight-bold">11:59:59 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 7 de 15, faltan 8</small></p><hr class="mb-1 mt-1"><p class="mb-1"></p><p class="mb-0">5 de octubre de 2026</p><p class="mb-0">11:59:59 pm</p><p></p><p class="mb-1 text-success"><small class="font-weight-bold">Hoy es el día 7 de 15, faltan 8</small></p></td><td class=" dt-170" style="display: none;"><div class="info-cliente"><p><i class="fa fa-user"></i>Comunicaciones Sala de Revisión Tutelas</p><p><i class="fa fa-envelope"></i>enviosrevision@corteconstitucional.gov.co</p><p><i class="fa fa-home"></i>Bogotá, D.C. - Bogotá, D.C.</p><hr class="mt-1 mb-1"><div class="info-cliente"><p class="font-weight-bold">Contacto:</p><p><i class="fa fa-user"></i>Ricardo Torres Castro</p></div></div></td><td class=" dt-250" style="display: none;"><p>Documento aceptado: Para tramite, gracias.</p><hr class="mb-1 mt-1"><p>T-3526653 AC OFICIO OPT-B-447-2026 AUTO 11-Sep-26 Requerimiento Información CONPES 4157</p><p></p><p><b>Canal:</b><span> Correo electrónico</span></p><p><b>Tipo requerimiento:</b><span> TUTELAS</span></p><p><b>Casos asociados: </b><span>2026-IE-035566,2026-IE-035552,2026-IE-035543</span></p><p><b>Entidad de control:</b> CORTE CONSTITUCIONAL</p><p></p></td><td class=" dt-120" style="display: none;"><p class="mb-0">14 de septiembre de 2026</p><p class="mb-0">04:17:36 pm</p></td><td class=" dt-350" style="display: none;"><table class="table-responsive" cellspacing="0" style="width:40rem; font-size:12px !important;" id="tblVerDetallesTarea"><tbody><tr><td style="width:8rem !important;"><b>Estado:</b></td><td>Cambio Fecha Vencimiento</td></tr><tr><td><b>Último evento:</b></td><td>15 de septiembre de 2026 10:31:52 am<br>JUAN SEBASTIAN BUITRAGO ALVARADO<br>Nueva fecha de vencimiento: 05/10/2026 23:59:59 <br></td></tr><tr></tr></tbody></table></td></tr></tbody></table><div id="tblGestionar_processing" class="dataTables_processing card" style="display: none;">Procesando...</div></div></div><div class="row"><div class="col-sm-12 col-md-5"><div class="dataTables_info" id="tblGestionar_info" role="status" aria-live="polite">Mostrando registros del 1 al 19 de un total de 19 registros</div></div><div class="col-sm-12 col-md-7"><div class="dataTables_paginate paging_simple_numbers" id="tblGestionar_paginate"><ul class="pagination"><li class="paginate_button page-item previous disabled" id="tblGestionar_previous"><a href="#" aria-controls="tblGestionar" data-dt-idx="0" tabindex="0" class="page-link">Anterior</a></li><li class="paginate_button page-item active"><a href="#" aria-controls="tblGestionar" data-dt-idx="1" tabindex="0" class="page-link">1</a></li><li class="paginate_button page-item next disabled" id="tblGestionar_next"><a href="#" aria-controls="tblGestionar" data-dt-idx="2" tabindex="0" class="page-link">Siguiente</a></li></ul></div></div></div></div></div>
    </div>
    <!--</div>
        </div>
    </div>-->
</div>

<div class="container-fluid oculto" id="containerGestionar">
    <div class="row">
        <div class="col-12" id="gestionarDetalle">
        </div>
    </div>
</div>

<div class="container-fluid oculto" id="containerFirmarRadicar">
</div>

<div class="container-fluid oculto" id="containerPorFirmar">
</div>

<!-- Modal -->
<div class="modal fade" id="modalGestionarTabla" tabindex="-1" role="dialog" aria-labelledby="modalGestionarTablaTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="modalGestionarTablaTitle"></h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">×</span>
                </button>
            </div>
            <div class="modal-body">
            </div>
            <!--<div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
            </div>-->
        </div>
    </div>
</div>
<!-- Modal -->
<div class="modal fade" id="modalPorFirmarTabla" tabindex="-1" role="dialog" aria-labelledby="modalPorFirmarTablaTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="modalPorFirmarTablaTitle"></h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">×</span>
                </button>
            </div>
            <div class="modal-body">
            </div>
            <!--<div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
            </div>-->
        </div>
    </div>
</div>
<!-- Modal -->
<div class="modal fade" id="modalPorFirmarRadicarTabla" tabindex="-1" role="dialog" aria-labelledby="modalPorFirmarRadicarTablaTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="modalPorFirmarRadicarTablaTitle"></h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">×</span>
                </button>
            </div>
            <div class="modal-body">
            </div>
            <!--<div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
            </div>-->
        </div>
    </div>
</div>
<!-- Modal -->
<div class="modal fade" id="modalResultadoFirmarRadicar" tabindex="-1" role="dialog" aria-labelledby="modalResultadoFirmarRadicarTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="modalResultadoFirmarRadicarTitle"></h5>
            </div>
            <div class="modal-body">
            </div>
            <div class="modal-footer">
                <button id="btnModalFirmarRadicar" type="button" class="btn btn-secondary" data-dismiss="modal">Cerrar</button>
            </div>
        </div>
    </div>
</div>
<!-- Modal -->
<div class="modal fade" id="modalExpediente" tabindex="-1" role="dialog" aria-labelledby="modalExpedienteTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="modalExpedienteTitle"></h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">×</span>
                </button>
            </div>
            <div class="modal-body">
            </div>
        </div>
    </div>
</div>
<!-- Modal -->
<div class="modal fade" id="modalDetalleFirma" tabindex="-1" role="dialog" aria-labelledby="modalExportarTitle" aria-hidden="true">
    <div class="modal-dialog modal-dialog modal-lg" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="modalExportarTitle"></h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">×</span>
                </button>
            </div>
            <div class="modal-body">
                <div id="modalBodyDetalleFirma">
                </div>
            </div>
        </div>
    </div>
</div>


            </div>
        </div>
    </div>
    <script src="/TMS.Solution.MENGESDOC/portal2/js?v=41arxdKjiT_8C8Sx7KV_k9YQgI_nFdpn-a7DqgdbUvk1"></script>

    <script>
        
TMS.SitioClasico='https://sgdea.mineducacion.gov.co/MENGESDOC/';
TMS.SitioSolution='https://sgdea.mineducacion.gov.co/TMS.Solution.MENGESDOC/(SwgUB8M7)/CR/es/';
TMS.SitioBase='https://sgdea.mineducacion.gov.co/TMS.Solution.MENGESDOC/';
 
        TMS.Apps =[{"Id":"CR","Nombre":"SGDEA"},{"Id":"GD","Nombre":"Versión anterior"}];
        TMS.Doc = {};
        TMS.Doc.ListaExtensiones = ['doc','docx','dot','dotx','xls','xltx','xlsx','pdf','pdf','msg','rar','zip','png','tiff','jpg','gif','ppt','pptx','jpeg','bmp','htm','html','trc','oft','jpg','png','txt','xltx','mpp','mpp','msg','mp4','docm','avi','avi','mp4','mp4','flv','mpg','mpeg'];
        TMS.Doc.TamMaximoAnexos = 99999999;
    </script>
    <script src="/TMS.Solution.MENGESDOC/Scripts/Portal/portal.js?v=1"></script>
    <script>
            </script>

    
    <script src="/TMS.Solution.MENGESDOC/MaM/js/Variables.js"></script>



    <script type="text/javascript">
        usuario = '1020821190';
		idOportunidad = TMS.Utils.GetQueryString('IdOp') || 0;
		idElemento = TMS.Utils.GetQueryString('IdEl') || 0;
    </script>

    <link href="/TMS.Solution.MENGESDOC/datatable/css?v=kHPB5EUUubvtsLzrcLfzxgns1vDr_UNNYdWZn2hn2VQ1" rel="stylesheet">

    <script src="/TMS.Solution.MENGESDOC/datatable/js?v=06qwIlyP1-GAGWMr9IyoY0qTqc2sgduQ2bE3NRAEo-81"></script>


    <link href="/TMS.Solution.MENGESDOC/MaM/css/HomeUsuario.css" rel="stylesheet">


    <script src="/TMS.Solution.MENGESDOC/MAM/js/knob/knob.js"></script>

    <script src="/TMS.Solution.MENGESDOC/MAM/js/chartjs/2.8/chart.min.js"></script>

    <script src="/TMS.Solution.MENGESDOC/MAM/js/chartjs/2.8/chartjs-plugin-datalabels.min.js"></script>


    <link href="/TMS.Solution.MENGESDOC/MaM/css/bootstrap-toggle/bootstrap-toggle.min.css" rel="stylesheet">

    <script src="/TMS.Solution.MENGESDOC/MAM/js/bootstrap-toggle/bootstrap-toggle.min.js"></script>


    <link href="/TMS.Solution.MENGESDOC/Content/bootstrap-fileinput/css/fileinput.css" rel="stylesheet">

    <script src="/TMS.Solution.MENGESDOC/Scripts/fileinput.js"></script>

    <script src="/TMS.Solution.MENGESDOC/Scripts/locales/es.js"></script>


    <link href="/TMS.Solution.MENGESDOC/MAM/css/timeline/timeline.css" rel="stylesheet">

    <link href="/TMS.Solution.MENGESDOC/MAM/css/table-responsive/table-responsive.css" rel="stylesheet">

    <link href="/TMS.Solution.MENGESDOC/MAM/css/cd-breadcrumb/cd-breadcrumb.css" rel="stylesheet">


    <link href="/TMS.Solution.MENGESDOC/MaM/css/Expediente.css" rel="stylesheet">


    <link href="/TMS.Solution.MENGESDOC/Content/magicsuggest-min.css" rel="stylesheet">

    <script src="/TMS.Solution.MENGESDOC/scripts/magicsuggest-min.js"></script>


    <link href="/TMS.Solution.MENGESDOC/MAM/BoostrapValidator/css/bootstrapValidator.css" rel="stylesheet">

    <script src="/TMS.Solution.MENGESDOC/MAM/BoostrapValidator/js/bootstrapValidator.js"></script>

    <script src="/TMS.Solution.MENGESDOC/MAM/BoostrapValidator/js/es_ES.js"></script>

    <script src="/TMS.Solution.MENGESDOC/Scripts/Seguimiento/SolicitudEventos.js"></script>


    <script src="/TMS.Solution.MENGESDOC/MAM/js/Utils.js?v=2019.00.564"></script><script src="/TMS.Solution.MENGESDOC/MAM/js/DocumentosPendientesXAprobar.js?v=2019.00.564"></script><script src="/TMS.Solution.MENGESDOC/MAM/js/DocsPorFirmarTabla.js?v=2019.00.564"></script><script src="/TMS.Solution.MENGESDOC/MAM/js/Expediente.js?v=2019.00.564"></script><script src="/TMS.Solution.MENGESDOC/MAM/js/GestionarTabla.js?v=2019.00.564"></script><script src="/TMS.Solution.MENGESDOC/MAM/js/TableroUsuario.js?v=2019.00.564"></script>



<div class="modal fade" id="TMSDialogModalDialog" style="display:none;" tabindex="-1"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><!--button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button--><h4 class="modal-title" id="TMSDialogModalTitulo">T&amp;MS</h4></div><div class="modal-body" id="TMSDialogModalContentDialog"></div><div class="modal-footer"><button type="button" class="btn btn-default" data-dismiss="modal">Cerrar</button><button type="button" class="btn btn-primary" id="TMSDialogHtmlModalOk">Guardar</button></div></div></div></div><div class="modal fade" id="TMSDialogModalDialogWoV" style="display:none;"><div class="modal-dialog modal-lg"><div class="modal-content"><div class="modal-header"><h4 class="modal-title" id="TMSDialogModalTituloWoV">T&amp;MS</h4><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button></div><div class="modal-body" id="TMSDialogModalContentDialogWoV"></div><div class="modal-footer"><button type="button" class="btn btn-default" id="TMSDialogHtmlModalOkWoV" data-dismiss="modal">Aceptar</button></div></div></div></div><div class="modal fade" id="TMSDialogModalDialogFind" style="display:none;"><div class="modal-dialog modal-lg" style="zoom: 70%"><div class="modal-content"><div class="modal-header"><h4 class="modal-title" id="TMSDialogModalTituloFind">T&amp;MS</h4><button type="button" class="close" data-dismiss="modal" aria-hidden="true">×</button></div><div class="modal-body" id="TMSDialogModalContentDialogFind"></div></div></div></div><div style="left: -1000px; overflow: scroll; position: absolute; top: -1000px; border-width: medium; border-style: none; border-color: currentcolor; border-image: none; box-sizing: content-box; height: 200px; margin: 0px; padding: 0px; width: 200px;"><div style="border-width: medium; border-style: none; border-color: currentcolor; border-image: none; box-sizing: content-box; height: 200px; margin: 0px; padding: 0px; width: 200px;"></div></div></body>



ahi colocaras en este box de buscar
<input type="search" class="form-control form-control-sm" placeholder="" aria-controls="tblGestionar" data-toggle="tooltip" data-placement="top" title="" data-original-title="mínimo 3 caracteres">

colocaras los radicados que te aparezcan en el excel, en la hoja Radicados a depurar, inspecciona el excel para que entiendas





