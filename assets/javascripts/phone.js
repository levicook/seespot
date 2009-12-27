
var Phone = {

  digits: {
    0: '0',
    1: '1',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PRS',
    8: 'TUV',
    9: 'WXY'
  },

  sanitize: function(phoneNumber) {
    phoneNumber = phoneNumber.replace(/[^0-9]/g, '');
    phoneNumber = phoneNumber.substring(0, 7);
    phoneNumber = $.map(phoneNumber, function(d) { return parseInt(d); });
    phoneNumber.sanitized = true;
    return phoneNumber;
  },

  // callback eg: function(word) { console.log(word) };
  eachWord: function(phoneNumber, callback, phoneNumberIdx, wordBuffer) {
    if(!phoneNumber.sanitized) {
      phoneNumber = this.sanitize(phoneNumber);
    }

    phoneNumberIdx = phoneNumberIdx || 0;
    wordBuffer = wordBuffer || new Array();

    // base case
    if(phoneNumberIdx == phoneNumber.length) {
      var word = wordBuffer.join('');
      callback(word);
      return
    }

    // recursive case
    for(var i = 0; i < 3; i++) {
      var digit = phoneNumber[phoneNumberIdx];
      wordBuffer[phoneNumberIdx] = this.digits[digit][i];
      this.eachWord(phoneNumber, callback, phoneNumberIdx+1, wordBuffer);
      if(digit == 0 || digit == 1) { return }
    }
  }

};
