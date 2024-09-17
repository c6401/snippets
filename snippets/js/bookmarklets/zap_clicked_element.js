javascript:function zap(e){e.preventDefault();e.stopPropagation();e.target.remove();document.removeEventListener('click',zap,true);};document.addEventListener('click', zap, true);
