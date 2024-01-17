document.addEventListener("DOMContentLoaded", function () {
    // 获取选择框元素
    const houseTypeSelect = document.querySelector('#houseTypeSelect');
    const elevatorSelect = document.querySelector('#ElevatorSelect');
    const managementSelect = document.querySelector('#ManagementSelect');

    // 初始化时，如果房屋类型选择公寓，将电梯和管理设置为无
    if (houseTypeSelect.value === '公寓') {
        elevatorSelect.value = '0';
        managementSelect.value = '0';
    }

    // 監聽房屋類型選項的變化
    houseTypeSelect.addEventListener('change', handleHouseTypeChange);

    function handleHouseTypeChange() {
        if (houseTypeSelect.value === '公寓') {
            // 如果選擇公寓，强制電梯和管理為無
            elevatorSelect.value = '0';
            managementSelect.value = '0';


        }
    }

    // 监听电梯选择框的变化事件
    elevatorSelect.addEventListener('change', handleElevatorChange);

    function handleElevatorChange() {
        if (houseTypeSelect.value === '公寓' && elevatorSelect.value === '1') {
            // 如果选择了公寓并且电梯选择了有电梯，弹出警告消息
            alert('公寓通常無電梯，請重新選擇！');
            // 将电梯重新设置为无电梯
            elevatorSelect.value = '0';
        }
    }

    // 监听管理选择框的变化事件
    managementSelect.addEventListener('change', handleManagementChange);

    function handleManagementChange() {
        if (houseTypeSelect.value === '公寓' && managementSelect.value === '1') {
            // 如果选择了公寓并且管理选择了有管理員，弹出警告消息
            alert('公寓通常無管理員，請重新選擇！');
            // 将管理重新设置为无管理員
            managementSelect.value = '0';
        }
    }
});
