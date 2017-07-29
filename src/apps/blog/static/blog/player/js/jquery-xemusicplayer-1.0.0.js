/*
* xeMusicPlayer Version 1.0.0
*
* Copyright 2013 @xeonne.de
* Licensed under the BSD license.
*/
(function($) {
    
    $.fn.xeMusicPlayer = function(options) {

        var settings = $.extend({}, $.fn.xeMusicPlayer.options, options);

        $.fn.xeMusicPlayer.options = settings;
        var songlist = settings.songlist;
        var mode = settings.mode;
        var main = $(this);
        var theme = settings.theme;
        var audio = null;
        var audioDuration = 0;
        var audioCurrentTime = 0;
        var setTime = null;
        var barWidth;
        var volumeWidth;
        var temp_volume = 1.0;

        init();
        start();
        
        function init(){
            if(theme == 1){
                if(mode == 1){
                    // Music player with Cover, Title, Artist, Timeline
                    main.html('<div class="xeMusic xeMusicPlayer"><div class="xeHeader"><div class="xeCover"><img src="xeMusicPlayer/img/cover-none.png" alt="" width="80" /></div><div class="xeMusicHeader"><div class="xeMusicHeaderText"><p class="xeTitle"></p><p class="xeTitleBy"></p></div><div class="xeSidebar"><div class="xeSidebarIcon xeTooltip"><span class="xeSidebarError"></span></div></div></div></div><div class="xePlayer"><div class="xeButton"><ul><li class="xePrevious disabled"><a href="javascript:;"></a></li><li class="xePlay"><a href="javascript:;"></a></li><li class="xeNext"><a href="javascript:;"></a></li></ul></div><div class="xeBar"><div class="xeBarTime"></div></div><div class="xeTime"><p>0:00</p></div></div><audio class="xeMP3"></audio></div>');
                }
                else if(mode == 2){
                    // Music player with Cover, Title, Artist, Timeline, Volume
                    main.html('<div class="xeMusic xeMusicPlayer xeMode2"> <div class="xeHeader"> <div class="xeCover"> <img src="xeMusicPlayer/img/cover-none.png" alt="" width="80" /> </div> <div class="xeMusicHeader"> <div class="xeMusicHeaderText"> <p class="xeTitle"></p> <p class="xeTitleBy"></p> </div> <div class="xeSidebar"> <div class="xeSidebarIcon xeTooltip"> <span class="xeSidebarError"></span> </div> </div> </div> </div> <div class="xePlayer"> <div class="xeButton"> <ul> <li class="xePrevious disabled"><a href="javascript:;"></a></li> <li class="xePlay"><a href="javascript:;"></a></li> <li class="xeNext"><a href="javascript:;"></a></li> </ul> </div> <div class="xeBar"> <div class="xeBarTime"></div> </div> <div class="xeTime"> <p>0:00</p> </div> <div class="xeVolume"> <ul> <li class="xeVolumeIcon xeVolumeOn"><a href="javascript:;"></a></li> </ul> </div> <div class="xeBarVolume"> <div class="xeBarVolumeLine"></div> </div> </div> <audio class="xeMP3"></audio> </div>');
                }
            }
            else if(theme == 2){
                if(mode == 1){
                    main.html('<div class="xeMusic xeMusicPlayer2"> <div class="xeHeader"> <div class="xeCover"> <img src="songs/Joe_Marson__The_Satisfied_Mind_-_09_-_Poor_St_John.jpg" alt="" width="31" /> </div> <div class="xeButton"> <ul> <li class="xePrevious disabled"><a href="javascript:;"></a></li> <li class="xePlay"><a href="javascript:;"></a></li> <li class="xeNext"><a href="javascript:;"></a></li> </ul> </div> </div> <div class="xePlayer"> <div class="xeBar"> <div class="xeBarTime"></div> </div> <div class="xeTime"> <p>0:00</p> </div> </div> <audio class="xeMP3"></audio> </div>');
                }
                else if(mode == 2){
                    main.html('<div class="xeMusic xeMusicPlayer2 xeMode2"> <div class="xeHeader"> <div class="xeCover"> <img src="songs/Joe_Marson__The_Satisfied_Mind_-_09_-_Poor_St_John.jpg" alt="" width="31" /> </div> <div class="xeButton"> <ul> <li class="xePrevious disabled"><a href="javascript:;"></a></li> <li class="xePlay"><a href="javascript:;"></a></li> <li class="xeNext"><a href="javascript:;"></a></li> </ul> </div> </div> <div class="xePlayer"> <div class="xeBar"> <div class="xeBarTime"></div> </div> <div class="xeTime"> <p>0:00</p> </div> <div class="xeVolume"> <ul> <li class="xeVolumeIcon xeVolumeOn"> <a href="javascript:;"></a> </li> </ul> </div> </div> <audio class="xeMP3"></audio> </div>');
                }
            }
            else if(theme == 3){
                if(mode == 1){
                    main.html('<div class="xeMusic xeMusicPlayer3"> <div class="xePlayer"> <div class="xeBarWithTime"> <div class="xeBar"> <div class="xeBarTime"></div> </div> </div> <div class="xeButtonWithVolume"> <div class="xeButton"> <ul> <li class="xePrevious disabled"><a href="javascript:;"></a></li> <li class="xePlay"><a href="javascript:;"></a></li> <li class="xeNext"><a href="javascript:;"></a></li> </ul> </div> <div class="xeTime"><p>0:00</p></div> </div> </div> <div class="xeHeader"> <div class="xeCover"> <img src="" alt="" width="70" /> </div> <div class="xeMusicHeader"> <div class="xeMusicHeaderText"> <p class="xeTitle"></p> <p class="xeTitleBy"></p> </div> </div> </div> <audio class="xeMP3"></audio> </div>');
                }
                else if(mode == 2){
                    main.html('<div class="xeMusic xeMusicPlayer3 xeMode2"> <div class="xePlayer"> <div class="xeBarWithTime"> <div class="xeBar"> <div class="xeBarTime"></div> </div> </div> <div class="xeButtonWithVolume"> <div class="xeButton"> <ul> <li class="xePrevious disabled"><a href="javascript:;"></a></li> <li class="xePlay"><a href="javascript:;"></a></li> <li class="xeNext"><a href="javascript:;"></a></li> </ul> </div> <div class="xeVolume"> <ul> <li class="xeVolumeIcon xeVolumeOn"> <a href="javascript:;"></a> </li> </ul> </div> <div class="xeTime"><p>0:00</p></div> </div> </div> <div class="xeHeader"> <div class="xeCover"> <img src="" alt="" width="70" /> </div> <div class="xeMusicHeader"> <div class="xeMusicHeaderText"> <p class="xeTitle"></p> <p class="xeTitleBy"></p> </div> </div> </div> <audio class="xeMP3"></audio> </div>');
                }
            }
            else if(theme == 4){
                if(mode == 1){
                    main.html('<div class="xeMusic xeMusicPlayer4"> <div class="xeCover"> <img src="" alt="" width="250" /> </div> <div class="xePlayer"> <div class="xeButton"> <ul> <li class="xePrevious disabled"><a href="javascript:;"></a></li> <li class="xePlay"><a href="javascript:;"></a></li> <li class="xeNext"><a href="javascript:;"></a></li> </ul> </div> <div class="xeBar"> <div class="xeBarTime"></div> </div> <div class="xeTime"><p>0:00</p></div> <div class="xeHeader"> <div class="xeMusicHeaderText"> <p class="xeTitle"></p> <p class="xeTitleBy"></p> </div> </div> </div> <audio class="xeMP3"></audio> </div>');
                }
                else if(mode == 2){
                    main.html('<div class="xeMusic xeMusicPlayer4 xeMode2"> <div class="xeCover"> <img src="" alt="" width="250" /> </div> <div class="xePlayer"> <div class="xeVolume"> <ul> <li class="xeVolumeIcon xeVolumeOn"> <a href="javascript:;"></a> </li> </ul> </div> <div class="xeButton"> <ul> <li class="xePrevious disabled"><a href="javascript:;"></a></li> <li class="xePlay"><a href="javascript:;"></a></li> <li class="xeNext"><a href="javascript:;"></a></li> </ul> </div> <div class="xeBar"> <div class="xeBarTime"></div> </div> <div class="xeTime"><p>0:00</p></div> <div class="xeHeader"> <div class="xeMusicHeaderText"> <p class="xeTitle"></p> <p class="xeTitleBy"></p> </div> </div> </div> <audio class="xeMP3"></audio> </div>');
                }
            }
            audio = main.find(".xeMP3")[0];
        }
        function start(){
            barWidth = main.find(".xeBarTime").width();
            volumeWidth = main.find(".xeBarVolumeLine").width();
            main.find(".xeBarTime").width(0);


            audio.addEventListener("abort", function() {
                main.find(".xeSidebar").show();
                main.find(".xeSidebarError").text("The loading of an audio is aborted!");
            });
            audio.addEventListener("stalled", function() {
                main.find(".xeSidebar").show();
                main.find(".xeSidebarError").text("Browser is trying to get media data, but data is not available!");
            });
            
            audio.addEventListener("play", function() {
                settings.isPlaying = true;
            });
            audio.addEventListener("error", function(e) {
                console.log("xeMusicPlayer-Error",e);
            });
            audio.addEventListener("pause", function() {
                settings.isPlaying = false;
            });
            audio.addEventListener("ended", function() {
                xeNext();
                settings.isPlaying = true;
            });
            audio.addEventListener("volumechange", function() {
                main.find(".xeBarVolumeLine").width( volumeWidth / (100 / (settings.volume*100)) );
                main.find(".xeVolumeIcon").removeClass("xeVolumeMute");
                main.find(".xeVolumeIcon").removeClass("xeVolumeOn");
                if(settings.volume == 0.0){
                    main.find(".xeVolumeIcon").addClass("xeVolumeMute");
                }
                else{
                    main.find(".xeVolumeIcon").addClass("xeVolumeOn");
                }
                settings.onChangeVolume.call( this );
            });
            audio.addEventListener("loadedmetadata", function() {
                main.find(".xeBarTime").width(0);
                main.find(".xeSidebar").hide();
                setAudio();
            });
            /* Play */
            main.find(".xePlay").click(function() {
                xePlayToggle();
            });
            /* Next */
            main.find(".xeNext").click(function() {
                xeNext();
                settings.onClickNext.call( this );
            });
            /* Previous */
            main.find(".xePrevious").click(function() {
                xePrevious();
                settings.onClickPrev.call( this );
            });
            /* Volume */
            main.find(".xeVolumeIcon").click(function() {
                if(audio.muted){
                    audio.muted = false;
                    audio.volume = temp_volume;
                    settings.volume = temp_volume;
                }else{
                    audio.muted = true;
                    audio.volume = 0.0;
                    temp_volume = settings.volume;
                    settings.volume = 0.0;
                }
            });
            main.find(".xeBar").click(function(e) {
                var parentOffset = $(e.target).offset(); 
                var relX = e.pageX - parentOffset.left;
                var t = relX / barWidth * 100;
                audio.currentTime = audioDuration / 100 * t;
            })
            main.find(".xeBarVolume").click(function(e) {
                var parentOffset = $(e.target).offset(); 
                var relX = e.pageX - parentOffset.left;
                var t = relX / barWidth * 100;
                audio.volume = (audioDuration / 100 * t)/100;
                settings.volume = audio.volume;
            })
            setSong(settings.songindex);
        }

        function setSong(index) {
            main.find(".xeBar").addClass("loader");
            if (songlist.length > index) {
                if (audio.canPlayType("audio/mpeg") != "" && songlist[index].mp3 != undefined) {
                    audio.src = songlist[index].mp3;
                    audio.load();
                }
                else if(audio.canPlayType("audio/ogg") != "" && songlist[index].ogg != undefined){
                    audio.src = songlist[index].ogg;
                    audio.load();
                }
                else{
                    console.log("xeMusicPlayer-Error","Can't play MPEG or OGG data!");
                    return;
                }
                if (songlist[index].title != undefined) {
                    main.find(".xeTitle").text(songlist[index].title);
                } else {
                    main.find(".xeTitle").text("");
                }
                main.find(".xeTitleLink").wrap(main.find(".xeTitle"));
                main.find(".xeTitleLink").remove();
                if (songlist[index].title_link != undefined) {
                    main.find(".xeTitle").wrap("<a href='"+songlist[index].title_link+"' class='xeTitleLink'></a>")
                }
                if (songlist[index].artist != undefined) {
                    main.find(".xeTitleBy").text(songlist[index].artist);
                } else {
                    main.find(".xeTitleBy").text("");
                }
                main.find(".xeTitleByLink").wrap(main.find(".xeTitleBy"));
                main.find(".xeTitleByLink").remove();
                if (songlist[index].artist_link != undefined) {
                    main.find(".xeTitleBy").wrap("<a href='"+songlist[index].title_link+"' class='xeTitleByLink'></a>")
                }
                if (songlist[index].cover != undefined) {
                    main.find(".xeCover img").attr("src", songlist[index].cover);
                } else {
                    main.find(".xeCover img").attr("src", "xeMusicPlayer/img/cover-none.png");
                }
            }
            settings.onChangeSongIndex.call( this );
        }
        function setTimer() {
            if (audio.currentTime != undefined && audio.currentTime != isNaN()) {
                audioCurrentTime = audio.currentTime;
                var currentTime = (audioCurrentTime / 60);
                currentTime = currentTime.toFixed(2);
                if (currentTime.indexOf(".") == -1) {
                    currentTime = currentTime + '.00';
                }
                currentTime = currentTime.split(".");
                var sec = Math.ceil(currentTime[1] / 100 * 60);
                if(sec == 60){ 
                    ++currentTime[0];
                    sec = 0;
                }
                main.find(".xeTime > p").text(currentTime[0] + ':' + (sec < 10 ? '0' + sec : sec));

                var t = audioCurrentTime * 100 / audioDuration;
                main.find(".xeBarTime").width(t / 100 * barWidth);
            } else {
                main.find(".xeTime > p").text("0:00");
                $(".xeBarTime").width(0);
            }
        }
        function setAudio() {
            if (audio.duration != undefined && audio.duration != isNaN()) {
                audioDuration = audio.duration;
                var durationTime = audioDuration / 60;
                durationTime = durationTime.toFixed(2);
                if (durationTime.indexOf(".") == -1) {
                    durationTime = durationTime + '.00';
                }
                durationTime = durationTime.split(".");
                var sec = Math.ceil(durationTime[1] / 100 * 60);
                main.find(".xeTime > p").text(durationTime[0] + ':' + (sec < 10 ? '0' + sec : sec));
            } else {
                main.find(".xeTime > p").text("-:--");
            }
            if (settings.isPlaying == true) {
                audio.play();
                if (setTime == null) {
                    setTime = window.setInterval(function(){setTimer()}, 50);
                }
            } else {
                audio.pause();
                if (setTime != null) {
                    window.clearInterval(setTime);
                    setTime = null;
                }
            }
            main.find(".xeBar").removeClass("loader");
        }
        function xePlayToggle() {
            if (settings.isPlaying == true) {
                xePause();
                settings.onClickPause.call( this );
            } else {
                xePlay();
                settings.onClickPlay.call( this );
            }
            settings.onChangePlaying.call( this );
        }
        function xePlay() {
            main.find(".xePlay").addClass("xeStop");
            audio.play();

            if (setTime == null) {
                setTime = window.setInterval(function(){setTimer()}, 50);
            }
        }
        function xePause() {
            main.find(".xePlay").removeClass("xeStop");
            audio.pause();
            if (setTime != null) {
                window.clearInterval(setTime);
                setTime = null;
            }
        }
        function xeNext() {
            if ((settings.songindex + 1) < songlist.length) {
                setSong(++settings.songindex);
                main.find(".xePrevious").removeClass("disabled");
            }
            if ((settings.songindex + 1) >= songlist.length) {
                main.find(".xeNext").addClass("disabled");
            }
        }
        function xePrevious() {
            if ((settings.songindex - 1) >= 0) {
                setSong(--settings.songindex);
                main.find(".xeNext").removeClass("disabled");
            }
            if ((settings.songindex) <= 0) {
                main.find(".xePrevious").addClass("disabled");
            }
        }
    };
    $.fn.xeMusicPlayer.options ={
        songlist: new Array(),
        mode: 1,
        theme: 1,
        sync: false,
        onClickPlay : function() {},
        onClickPause : function() {},
        onClickPrev : function() {},
        onClickNext: function() {},
        onChangeVolume : function() {},
        onChangePlaying : function() {},
        onChangeSongIndex : function() {},
        songindex: 0,
        volume: 1.0,
        isPlaying: false
    }
})(jQuery);