
// 获取按钮和弹出式面板元素
const showFilterOptionsButton = document.getElementById('showFilterOptions');
const overlay = document.getElementById('overlay');
const popup = document.getElementById('popup');
const confirmPopupButton = document.getElementById('confirmPopup');

// 添加按钮点击事件监听器
showFilterOptionsButton.addEventListener('click', () => {
    // 显示遮罩层和弹出式面板
    overlay.style.display = 'block';
    popup.style.display = 'block';
});

// 添加关闭弹出式面板的功能，点击遮罩层或"確定"按钮都会关闭
overlay.addEventListener('click', () => {
    overlay.style.display = 'none';
    popup.style.display = 'none';
});

confirmPopupButton.addEventListener('click', () => {
    overlay.style.display = 'none';
    popup.style.display = 'none';
    // 在此处执行用户点击“確定”后的操作
});
