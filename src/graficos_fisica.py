import matplotlib
matplotlib.use('Agg')  # Configura o Matplotlib para rodar em background sem abrir janelas de interface
import matplotlib.pyplot as plt
import io
import base64

def gerar_grafico_mru(v, t):
    """
    Gera um gráfico v x t para Movimento Retilíneo Uniforme (Velocidade Constante)
    e retorna a imagem codificada em Base64.
    """
    plt.figure(figsize=(5, 3))
    
    # Desenha a linha da velocidade constante
    plt.plot([0, t], [v, v], color='#004b87', linewidth=3, label=f'v = {v} m/s')
    
    # Preenche a área sob a curva (que representa a distância)
    plt.fill_between([0, t], [v, v], color='#004b87', alpha=0.15)
    
    # Configurações dos eixos gráficos
    plt.xlim(0, t + 1)
    plt.ylim(0, v + 5)
    plt.xlabel('Tempo (s)', fontsize=10)
    plt.ylabel('Velocidade (m/s)', fontsize=10)
    plt.title('Gráfico Velocidade vs Tempo (MRU)', fontsize=11, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Destaca os pontos importantes nos eixos
    plt.axvline(x=t, color='gray', linestyle=':')
    plt.axhline(y=v, color='gray', linestyle=':')
    plt.text(t + 0.1, v / 2, f'Δt = {t}s', color='black', fontsize=9)
    
    # Converte o gráfico em imagem de bytes na memória
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=100)
    buf.seek(0)
    plt.close()
    
    # Codifica em string Base64 para embutir direto na tag <img src="..."> do HTML
    imagem_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{imagem_base64}"
