odoo.define('quiz_idle_timer.timer', function (require) {
    var publicWidget = require('web.public.widget');
    var idleTimer = this.$('.quiz_idle_timer');
    publicWidget.registry.QuizIdleTimer = publicWidget.Widget.extend({
        selector: '.o_survey_background',
        start: function() {
            this.inactiveTime = idleTimer.data('idleTime')
            this.countdownTime = idleTimer.data('countdownTime')
            this.countdownTimer = this.$('#idle_timer')
            this.idleTime = 0;
            this.countdown = 0;
            this.startTimer();
            $(document).on('mousemove keypress', this.resetIdleTime.bind(this));
        },
        startTimer: function(){
            this.idleInterval = setInterval(this.timerIncrement.bind(this), 1000)
        },
        timerIncrement: function(){
            this.idleTime++;
            if (this.idleTime > this.inactiveTime) {
                this.countdown++;
                var minutes = Math.floor(this.countdown / 60);
                var minuteScreen = minutes.toString().padStart(2, '0');
                var secondScreen = this.countdown.toString().padStart(2, '0')
                this.countdownTimer.text(minuteScreen + ':' + secondScreen)
                if (this.idleTime >= this.inactiveTime + this.countdownTime){
                    this.$('.btn-primary').click()
                    this.resetIdleTime()
                }
            }
        },
        resetIdleTime: function(){
            this.idleTime = 0
            this.countdown = 0
            this.countdownTimer.text('00:00')
        }
    })
});