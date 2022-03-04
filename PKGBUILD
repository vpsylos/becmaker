# Maintainer: Vangelis Psylos <vpsylos@gmail.com>
pkgname="becmaker"
pkgver="1.0"
pkgrel="1"
pkgdesc="Tool to create break-even charts for the IB Business Management course."
arch=("x86_64")
depends=("python>=3.6.0")
makedepends=("gendesk")
license=("custom")
source=("becmaker.py" "application-becmaker.png")
sha512sums=("SKIP" "SKIP")

package () {
    gendesk -f -n --pkgname "$pkgname" --pkgdesc "$pkgdesc"
    install -Dm644 "$pkgname.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"
    install -Dm644 "${srcdir}/application-$pkgname.png" "$pkgdir/usr/share/pixmaps/$pkgname.png"
    pip install PySimpleGUIQt
    pip install matplotlib
    mkdir -p "${pkgdir}/usr/bin"
    cp "${srcdir}/becmaker.py" "${pkgdir}/usr/bin/becmaker"
    chmod +x "${pkgdir}/usr/bin/becmaker"
    printf "In order to use becmaker, run \n\t becmaker \nin terminal.\n"
}
