// cityfunctions.js
// 获取城市和鄉鎮市區的選擇框元素
const citySelect = document.getElementById("city");
const cityAreaSelect = document.getElementById("cityarea");

// 定義不同城市的鄉鎮市區選項
const cityOptions = {
    "臺北市": ["中正區", "大同區", "中山區", "松山區", "大安區", "萬華區", "信義區", "士林區", "北投區", "內湖區", "南港區", "文山區"],
    "新北市": ["板橋區", "汐止區", "新店區", "永和區", "中和區", "土城區", "三峽區", "樹林區", "鶯歌區", "三重區", "新莊區", "泰山區", "林口區", "蘆洲區", "五股區", "八里區", "淡水區"]
};

// 將城市選擇框的選項填充
function populateCityOptions() {
    citySelect.innerHTML = '<option value="" selected>請選擇縣市</option>';
    for (const city in cityOptions) {
        const option = document.createElement("option");
        option.value = city;
        option.textContent = city;
        citySelect.appendChild(option);
    }
}

// 根據所選城市填充鄉鎮市區選項
function populateCityAreas(selectedCity) {
    cityAreaSelect.innerHTML = '<option value="" selected disabled hidden>請選擇鄉鎮市區</option>';
    const selectedCityAreas = cityOptions[selectedCity];
    if (selectedCityAreas) {
        for (const area of selectedCityAreas) {
            const option = document.createElement("option");
            option.value = area;
            option.textContent = area;
            cityAreaSelect.appendChild(option);
        }
    }
}

// 添加城市選擇框的事件監聽器
citySelect.addEventListener("change", function () {
    const selectedCity = citySelect.value;
    populateCityAreas(selectedCity);
});

// 初始化頁面載入時的預設值
document.addEventListener("DOMContentLoaded", function () {
    populateCityOptions();
    populateCityAreas(""); // 空字符串表示預設值
});

// 添加表單提交前的驗證
document.querySelector("form").addEventListener("submit", function (e) {
    if (citySelect.value === "" || cityAreaSelect.value === "") {
        alert("請確保您已選擇縣市和鄉鎮市區。");
        e.preventDefault(); // 阻止表單提交
    }
});

// 顯示進階篩選選項
const showFilterOptionsButton = document.getElementById("showFilterOptions");
const overlay = document.getElementById("overlay");
const popup = document.getElementById("popup");
const confirmPopupButton = document.getElementById("confirmPopup");

showFilterOptionsButton.addEventListener("click", () => {
    overlay.style.display = 'block';
    popup.style.display = 'block';
});

overlay.addEventListener("click", () => {
    overlay.style.display = 'none';
    popup.style.display = 'none';
});

confirmPopupButton.addEventListener("click", () => {
    overlay.style.display = 'none';
    popup.style.display = 'none';
    // 在此處執行用戶點擊“確定”後的操作
});

function citychange() {
    var citySelect = document.getElementById("city");
    populateCityAreas(citySelect.value);
}

// 初始化页面加载时的默认值
document.addEventListener("DOMContentLoaded", function () {
    populateCityAreas(""); // 空字符串表示默认值
});

console.log(populateCityAreas("臺北市"))