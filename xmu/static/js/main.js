// 处理导航点击事件，实现平滑滚动
function handleNavClick(event, el) {
    event.preventDefault();  // 阻止默认的锚点跳转行为

    const targetId = el.getAttribute("data-target");  // 获取目标 section 的 id
    const targetEl = document.getElementById(targetId);  // 获取目标 section 元素

    if (targetEl) {
        // 确保滚动行为生效，平滑滚动到目标元素
        targetEl.scrollIntoView({
            behavior: "smooth",  // 启用平滑滚动
            block: "start"       // 定位到目标区域顶部
        });
    }

    // 关闭菜单（如果是移动端或响应式菜单）
    const nav = document.querySelector('nav');
    if (nav.classList.contains('active')) {
        nav.classList.remove('active');
    }
}


function handleNavClick2(event, el) {
    // 注释掉 event.preventDefault() 来允许页面跳转
    // event.preventDefault();  // 阻止默认的锚点跳转行为

    const targetId = el.getAttribute("data-target");  // 获取目标 section 的 id
    const targetEl = document.getElementById(targetId);  // 获取目标 section 元素

    if (targetEl) {
        targetEl.scrollIntoView({
            behavior: "smooth",  // 启用平滑滚动
            block: "start"       // 定位到目标区域顶部
        });
    }

    // 关闭菜单（如果是移动端或响应式菜单）
    const nav = document.querySelector('nav');
    if (nav.classList.contains('active')) {
        nav.classList.remove('active');
    }
}



// 更新导航栏高亮状态
function updateActiveNav(el) {
    const navLinks = document.querySelectorAll("nav ul li a[data-target]");

    // 移除所有链接的 active 类
    navLinks.forEach(link => {
        link.classList.remove("active");
    });

    // 给点击的链接添加 active 类
    el.classList.add('active');
}

// 切换导航菜单的显示/隐藏（用于移动端）
function toggleMenu() {
    const nav = document.querySelector('nav');
    const hamburgerMenu = document.querySelector('.hamburger-menu');

    // 切换 active 类
    nav.classList.toggle('active');
    hamburgerMenu.classList.toggle('active');
}

// 处理下拉菜单点击事件
function toggleDropdown(event) {
    event.preventDefault();
    const dropdown = event.target.closest('a').nextElementSibling;
    dropdown.classList.toggle('show');

    // 关闭其他下拉菜单
    document.querySelectorAll('.dropdown-content').forEach(function(content) {
        if (content !== dropdown) {
            content.classList.remove('show');
        }
    });
}

// 页面滚动时更新高亮状态
function updateScrollHighlight() {
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll("nav ul li a[data-target]");

    let currentId = "hero";  // 默认是 Home 区域

    sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        if (rect.top <= 100 && rect.bottom > 100) {
            currentId = section.id;
        }
    });

    navLinks.forEach(link => {
        if (link.getAttribute("data-target") === currentId) {
            link.classList.add("active");
        } else {
            link.classList.remove("active");
        }
    });
}

// 页面滚动时更新高亮状态
window.addEventListener("scroll", updateScrollHighlight);

// 页面加载时执行一次，确保高亮第一个区块
window.addEventListener("load", updateScrollHighlight);

// 页面滚动时隐藏/显示导航栏
let lastScrollTop = 0; // 上次滚动的位置
let navbar = document.querySelector("header"); // 获取导航栏

window.addEventListener("scroll", function() {
    let currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    if (currentScroll > lastScrollTop && currentScroll > navbar.offsetHeight) {
        // 向下滚动，隐藏导航栏
        navbar.style.top = `-${navbar.offsetHeight}px`; // 隐藏导航栏
    } else if (currentScroll < lastScrollTop) {
        // 向上滚动，显示导航栏
        navbar.style.top = "0"; // 显示导航栏
    }

    // 更新滚动位置
    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
});
