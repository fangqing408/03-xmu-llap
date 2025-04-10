// 点击导航或按钮，平滑滚动
function handleNavClick(event, el) {
    event.preventDefault();  // 阻止默认跳转

    const targetId = el.getAttribute("data-target");
    const targetEl = document.getElementById(targetId);

    if (targetEl) {
        const rect = targetEl.getBoundingClientRect();

        // 如果已经在该区域内，不滚动
        if (rect.top <= 100 && rect.bottom > 100) {
            return;
        }

        targetEl.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    }
}

// 更新导航高亮状态
function updateActiveNav() {
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


// 页面滚动时更新高亮
window.addEventListener("scroll", updateActiveNav);

// 页面初始加载时也执行一次，确保 Home 被高亮
window.addEventListener("load", updateActiveNav);
