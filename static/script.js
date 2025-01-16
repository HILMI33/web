// Script untuk meningkatkan interaktivitas halaman

document.addEventListener("DOMContentLoaded", function() {
    // Konfirmasi sebelum menghapus produk
    const deleteLinks = document.querySelectorAll("a[href*='delete']");

    deleteLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            const confirmation = confirm("Yakin ingin menghapus produk ini?");
            if (!confirmation) {
                event.preventDefault();
            }
        });
    });

    // Animasi smooth scroll untuk navigasi (jika diperlukan)
    const navLinks = document.querySelectorAll("nav a");

    navLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            event.preventDefault();
            const targetId = this.getAttribute("href").slice(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop,
                    behavior: "smooth"
                });
            } else {
                window.location.href = this.getAttribute("href");
            }
        });
    });
});
