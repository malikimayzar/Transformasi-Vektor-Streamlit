import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def vektor_shearing(vektor, jenis_shearing, k):
    if jenis_shearing == "x":
        shearing_matrix = np.array([[1, k],
                                    [0, 1]])
    elif jenis_shearing == "y":
        shearing_matrix = np.array([[1, 0],
                                    [k, 1]])
    else:
        raise ValueError("Jenis shearing harus 'x' atau 'y'.")

    vektor_hasil = shearing_matrix @ vektor
    return vektor_hasil


def animasi_shearing(vektor_awal, vektor_akhir, nama_file="HasilTransformasi/animasi_shearing.gif"):
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True)
    ax.set_aspect('equal')
    ax.set_title("Shearing")

    # Vektor awal (garis biru)
    quiver = ax.quiver(0, 0, vektor_awal[0], vektor_awal[1], angles='xy', scale_units='xy', scale=1, color='blue')

    def update(frame):
        t = frame / 30
        v_interpolasi = (1 - t) * vektor_awal + t * vektor_akhir
        quiver.set_UVC(v_interpolasi[0], v_interpolasi[1])
        return [quiver]  

    anim = FuncAnimation(fig, update, frames=31, interval=50, blit=False)

    plt.draw()
    plt.pause(0.1)  # Wajib untuk Streamlit
    anim.save(nama_file, writer='pillow', fps=20)
    plt.close(fig)
