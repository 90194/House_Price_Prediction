
// 获取选择框元素
const bedroomSelect = document.querySelector('select[name="bedroom_pattern"]');
const livingRoomSelect = document.querySelector('select[name="livingRoom_pattern"]');
const bathroomSelect = document.querySelector('select[name="bathroom_pattern"]');

// 监听选择框的变化事件
bedroomSelect.addEventListener('change', validateSelection);
livingRoomSelect.addEventListener('change', validateSelection);
bathroomSelect.addEventListener('change', validateSelection);

// 验证函数
function validateSelection() {
  const bedroomCount = parseInt(bedroomSelect.value);
  const livingRoomCount = parseInt(livingRoomSelect.value);
  const bathroomCount = parseInt(bathroomSelect.value);

  // 驗證客廳數和衛浴數是否小於等于房間數
  if (livingRoomCount > bedroomCount) {
    alert('客廳數量不能超過房間數量！');
    livingRoomSelect.value = '1'; // 將客廳數重置為1
  }

  if (bathroomCount > bedroomCount) {
    alert('衛浴數量不能超過房間數量！');
    bathroomSelect.value = '1'; // 將衛浴数重置为1
  }
}
