# Como aplicar o novo visual no WordPress/Elementor

## 1. Colar o CSS
Elementor → ☰ → **Configurações do Site → CSS Personalizado** → cole todo o conteúdo de `aldeia-literaria.css` → Publicar.
(Alternativa: Aparência → Personalizar → CSS adicional.) Mantém as cores/fontes que você já usa (vermelho #DF3F21, azul #083656, GFS Didot + Montserrat).

## 2. Já funciona sozinho (sem classes)
Botões, acordeão do FAQ, menu do cabeçalho (fixo, com sublinhado), tipografia e responsivo.

## 3. Classes para adicionar (Avançado → Classes CSS)
| Seção/elemento | Classe |
|---|---|
| Container do cabeçalho | `al-header` |
| Container do hero (fundo azul) | `al-hero` |
| Título H1 do hero | (automático dentro de `al-hero`) |
| Selo "Extensão universitária" | `al-badge` |
| Linha de chips (100% online…) | `al-chips` e cada chip `al-chip` |
| Cartão "Próxima turma" | `al-hero-card` |
| Faixa de números (+500…) | `al-stats` com filhos `al-stat` |
| Qualquer seção | `al-section` (`al-section--alt` cinza, `al-section--navy` azul) |
| Subtítulo vermelho pequeno | `al-eyebrow` · Títulos: `al-title` · Texto: `al-lead` |
| Grade de cartões | `al-grid-2` / `al-grid-3` / `al-grid-4` no container pai; cada cartão `al-card` |
| Professores | `al-card al-teacher` |
| Módulos | `al-card al-module` (número em `al-num`, tags em `al-meta`) |
| Preços | `al-card al-price` (o do meio `al-price--featured`) |
| Certificação | seção com `al-section--navy al-cert` |
| CTA WhatsApp | `al-cta` · Rodapé: `al-footer` |
| Botão contorno / branco | `al-btn--outline` / `al-btn--light` |

Dica: no Elementor use Containers (Flexbox) com "Layout → Largura do conteúdo: 1160px" e desative o espaçamento próprio dos containers filhos das grades.

## 4. Pré-visualização
Abra `preview/index.html` no navegador. Ela usa exatamente o mesmo CSS.
