function drawCavans(max) {
    function Dot() {//dot style
        this.x = 0;
        this.y = 0;
        this.draw = function (ctx) {
            ctx.save();
            ctx.beginPath();
            ctx.fillStyle = 'rgba(255, 255, 255, 1)';
            ctx.arc(this.x, this.y, 3, 0, Math.PI * 2, false);
            ctx.fill();
            ctx.restore();
        };
    }

    function text(process) {//text
        ctx.save();
        ctx.rotate(10 * deg0);
        ctx.fillStyle = '#FFFFFF';
        ctx.font = '80px Microsoft yahei';
        ctx.textAlign = 'center';
        ctx.textBaseLine = 'top';
        ctx.fillText(process, 0, 10);
        ctx.restore();
    }
    var canvas = document.getElementById('canvas'),
    ctx = canvas.getContext('2d'),
    cWidth = canvas.width,
    cHeight = canvas.height,
    score = 0
    stage = ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent'],
    radius = 150,
    deg0 = Math.PI / 9,
    deg1 = Math.PI * 11 / 45;
    var dot = new Dot(),
    angle = 0,
    credit = 0;
    ctx.save();
    ctx.clearRect(0, 0, cWidth, cHeight);
    ctx.translate(cWidth / 2, cHeight / 2);
    ctx.rotate(8 * deg0);
    dot.x = radius * Math.cos(angle);
    dot.y = radius * Math.sin(angle);
    dot.draw(ctx);
    text(credit);
    ctx.save();
    ctx.beginPath();
    ctx.lineWidth = 3;
    ctx.strokeStyle = 'rgba(255, 255, 255, .5)';
    ctx.arc(0, 0, radius, 0, angle, false);
    ctx.stroke();
    ctx.restore();
    ctx.save(); //中间刻度层
    ctx.beginPath();
    ctx.strokeStyle = 'rgba(255, 255, 255, .2)';
    ctx.lineWidth = 10;
    ctx.arc(0, 0, 135, 0, 11 * deg0, false);
    ctx.stroke();
    ctx.restore();

    ctx.save(); // 刻度线
    for (var i = 0; i < 6; i++) {
        ctx.beginPath();
        ctx.lineWidth = 2;
        ctx.strokeStyle = 'rgba(255, 255, 255, .3)';
        ctx.moveTo(140, 0);
        ctx.lineTo(130, 0);
        ctx.stroke();
        ctx.rotate(deg1);
    }
    ctx.restore();

    ctx.save(); // 细分刻度线
    for (i = 0; i < 25; i++) {
        if (i % 5 !== 0) {
            ctx.beginPath();
            ctx.lineWidth = 2;
            ctx.strokeStyle = 'rgba(255, 255, 255, .1)';
            ctx.moveTo(140, 0);
            ctx.lineTo(133, 0);
            ctx.stroke();
        }
            ctx.rotate(deg1 / 5);
        }
    ctx.restore();

    ctx.save(); //digital
    ctx.rotate(Math.PI / 2);
    var interval=max/5
    for (i = 0; i < 6; i++) {
        ctx.fillStyle = 'rgba(255, 255, 255, 1)';
        ctx.font = '10px Microsoft yahei';
        ctx.textAlign = 'center';
        ctx.fillText(0 + interval * i, 0, -115);
        ctx.rotate(deg1);
    }
    ctx.restore();
    ctx.save(); //rate 
    ctx.rotate(Math.PI / 2 + deg0);
    for (i = 0; i < 5; i++) {
        ctx.fillStyle = 'rgba(255, 255, 255, 1)';
        ctx.font = '10px Microsoft yahei';
        ctx.textAlign = 'center';
        ctx.fillText(stage[i], 5, -115);
        ctx.rotate(deg1);
    }
    ctx.restore();

    ctx.save(); //信用阶段及评估时间文字
    ctx.rotate(10 * deg0);
    ctx.fillStyle = '#fff';
    ctx.font = '28px Microsoft yahei';
    ctx.textAlign = 'center';
    if (score < 500) {
        ctx.fillText('Poor', 0, 40);
    } else if (score < 600 && score >= 500) {
        ctx.fillText('Fair', 0, 40);
    } else if (score < 700 && score >= 600) {
        ctx.fillText('Good', 0, 40);
    } else if (score < 800 && score >= 700) {
        ctx.fillText('Very Good', 0, 40);
    } else if (score <= 900 && score >= 800) {
        ctx.fillText('Excellent', 0, 40);
    }

    ctx.fillStyle = '#faaf80';
    ctx.font = '14px Microsoft yahei';
    ctx.fillText(CurentTime(), 0, 60);

    ctx.fillStyle = '#faaf80';
    ctx.font = '14px Microsoft yahei';
    ctx.fillText('Score', 0, -60);
    ctx.restore();


        //最外层轨道
    ctx.beginPath();
    ctx.strokeStyle = 'rgba(255, 255, 255, .4)';
    ctx.lineWidth = 3;
    ctx.arc(0, 0, radius, 0, 11 * deg0, false);
    ctx.stroke();
    ctx.restore();


}
drawCavans(1000)







console.log()
//-----------------------static---------------------------
console.log()



function liveUpdate(max,current) {
    var canvas = document.getElementById('canvas'),
        ctx = canvas.getContext('2d'),
        cWidth = canvas.width,
        cHeight = canvas.height,
        score = current
        stage = ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent'],
        radius = 150,
        interval=max/5
        deg0 = Math.PI / 9,
        deg1 = Math.PI * 11 / 45;

    
        var dot = new Dot(),
            dotSpeed = 0.03,
            textSpeed = Math.round(dotSpeed * interval / deg1),
            angle = 0,
            credit = 0;




        (function drawFrame() {

            ctx.save();
            ctx.clearRect(0, 0, cWidth, cHeight);
            ctx.translate(cWidth / 2, cHeight / 2);
            ctx.rotate(8 * deg0);

            dot.x = radius * Math.cos(angle);
            dot.y = radius * Math.sin(angle);

            var aim = (score - 0) * deg1 / interval;
            if (angle < aim) {
                angle += dotSpeed;
            }
            dot.draw(ctx);

            if (credit < score - textSpeed) {
                credit += textSpeed;
            } else if (credit >= score - textSpeed && credit < score) {
                credit += 1;
            }
            text(credit);

            ctx.save();
            ctx.beginPath();
            ctx.lineWidth = 3;
            ctx.strokeStyle = 'rgba(255, 255, 255, .5)';
            ctx.arc(0, 0, radius, 0, angle, false);
            ctx.stroke();
            ctx.restore();


            // window.requestAnimationFrame(drawFrame);

            ctx.save(); //中间刻度层
            ctx.beginPath();
            ctx.strokeStyle = 'rgba(255, 255, 255, .2)';
            ctx.lineWidth = 10;
            ctx.arc(0, 0, 135, 0, 11 * deg0, false);
            ctx.stroke();
            ctx.restore();

            ctx.save(); // 刻度线
            for (var i = 0; i < 6; i++) {
                ctx.beginPath();
                ctx.lineWidth = 2;
                ctx.strokeStyle = 'rgba(255, 255, 255, .3)';
                ctx.moveTo(140, 0);
                ctx.lineTo(130, 0);
                ctx.stroke();
                ctx.rotate(deg1);
            }
            ctx.restore();

            ctx.save(); // 细分刻度线
            for (i = 0; i < 25; i++) {
                if (i % 5 !== 0) {
                    ctx.beginPath();
                    ctx.lineWidth = 2;
                    ctx.strokeStyle = 'rgba(255, 255, 255, .1)';
                    ctx.moveTo(140, 0);
                    ctx.lineTo(133, 0);
                    ctx.stroke();
                }
                ctx.rotate(deg1 / 5);
            }
            ctx.restore();

            ctx.save(); //digital
            ctx.rotate(Math.PI / 2);
            for (i = 0; i < 6; i++) {
                ctx.fillStyle = 'rgba(255, 255, 255, 1)';
                ctx.font = '10px Microsoft yahei';
                ctx.textAlign = 'center';
                ctx.fillText(0 + interval * i, 0, -115);
                ctx.rotate(deg1);
            }
            ctx.restore();

            ctx.save(); //rate 
            ctx.rotate(Math.PI / 2 + deg0);
            for (i = 0; i < 5; i++) {
                ctx.fillStyle = 'rgba(255, 255, 255, 1)';
                ctx.font = '10px Microsoft yahei';
                ctx.textAlign = 'center';
                ctx.fillText(stage[i], 5, -115);
                ctx.rotate(deg1);
            }
            ctx.restore();

            ctx.save(); 
            ctx.rotate(10 * deg0);
            ctx.fillStyle = '#fff';
            ctx.font = '28px Microsoft yahei';
            ctx.textAlign = 'center';
            if (score < 0+interval) {
                ctx.fillText('Poor', 0, 40);
            } else if (score < 0+2*interval && score >= 0+interval) {
                ctx.fillText('Fair', 0, 40);
            } else if (score < 3*interval && score >= 2*interval) {
                ctx.fillText('Good', 0, 40);
            } else if (score < 4*interval && score >= 3*interval) {
                ctx.fillText('Very Good', 0, 40);
            } else if (score <= 5*interval && score >= 4*interval) {
                ctx.fillText('Excellent', 0, 40);
            }

            ctx.fillStyle = '#faaf80';
            ctx.font = '14px Microsoft yahei';
            ctx.fillText(CurentTime(), 0, 60);

            ctx.fillStyle = '#faaf80';
            ctx.font = '14px Microsoft yahei';
            ctx.fillText('Score', 0, -60);
            ctx.restore();


            //最外层轨道
            ctx.beginPath();
            ctx.strokeStyle = 'rgba(255, 255, 255, .4)';
            ctx.lineWidth = 3;
            ctx.arc(0, 0, radius, 0, 11 * deg0, false);
            ctx.stroke();
            ctx.restore();
            console.log(score)


            if (credit < score) {
                window.requestAnimationFrame(drawFrame);
            }







        })();
    


    function Dot() {//dot style
        this.x = 0;
        this.y = 0;
        this.draw = function (ctx) {
            ctx.save();
            ctx.beginPath();
            ctx.fillStyle = 'rgba(255, 255, 255, 1)';
            ctx.arc(this.x, this.y, 3, 0, Math.PI * 2, false);
            ctx.fill();
            ctx.restore();
        };
    }

    function text(process) {//text
        ctx.save();
        ctx.rotate(10 * deg0);
        ctx.fillStyle = '#FFFFFF';
        ctx.font = '80px Microsoft yahei';
        ctx.textAlign = 'center';
        ctx.textBaseLine = 'top';
        ctx.fillText(process, 0, 10);
        ctx.restore();
    }
};

// liveUpdate(800,650)



function CurentTime() {
    var now = new Date();

    var year = now.getFullYear();
    var month = now.getMonth() + 1;
    var day = now.getDate();

    var hh = now.getHours();
    var mm = now.getMinutes();

    var clock = year + "-";

    if (month < 10)
        clock += "0";

    clock += month + "-";

    if (day < 10)
        clock += "0";

    clock += day + " ";

    if (hh < 10)
        clock += "0";

    clock += hh + ":";
    if (mm < 10) clock += '0';
    clock += mm;
    return (clock);
};
var updateAll = function () {

    var getIP = function () {
        $.getJSON("https://api.ipify.org?format=jsonp&callback=?",
            function (json) {
                var ip = json.ip
                $("#ip").html(json.ip)


                var api_key = "at_5ytLxnM93tT3Q2oWkOBoKidXWan3W";
                var getLocation = function () {
                    $.ajax({

                        url: "https://geo.ipify.org/api/v1",

                        data: { apiKey: api_key, ipAddress: ip },
                        success: function (data) {
                            console.log(data)
                            console.log(typeof (data))
                            console.log(data["location"])
                            var country = data["location"]["country"]
                            var region = data["location"]["region"]
                            var lat = data["location"]["lat"]
                            var lng = data["location"]["lng"]
                            var city = data["location"]["city"]
                            var time = data["location"]["timezone"]
                            var isp = data["isp"]
                            var address = city + " " + region + " " + country
                            $("#location").text(address)
                            $("#isp").text(isp)


                        }
                    });
                };
                getLocation()


            }
        );
    };
    getIP()
    liveUpdate(800,650)
};


$("#go").on("mouseenter", function () {
    $(this).css("font-weight", "bold")
})
$("#go").on("mouseleave", function () {
    $(this).css("font-weight", "normal")
})
$("#go").on("click", updateAll)







