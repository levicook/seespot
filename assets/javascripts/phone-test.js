
module('Phone');

test('eachWord("0123")', function() {
  var expected = '01AD,01AE,01AF,01BD,01BE,01BF,01CD,01CE,01CF'.split(',');
  var observed = new Array();
  Phone.eachWord('0123', function(word) {
    observed.push(word);
  });
  equal(observed.length, expected.length, "results count should equal");
  // Order isn't really guaranteed, so these might appropriate in the future.
  // expected.sort(); 
  // observed.sort();
  $.each(expected, function(i) {
    equal(observed[i], this);
  });
});

test('results ceiling', function() {
  var count = 0;
  Phone.eachWord('9999999999999', function() { count++; });
  equal(count, Math.pow(3, 7), "results count should equal");
});

// TODO Phone.sanitize
