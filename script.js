// Book data storage
let bookData = {
    title: '',
    author: '',
    pages: []
};

// DOM elements
const bookTitleInput = document.getElementById('bookTitle');
const bookAuthorInput = document.getElementById('bookAuthor');
const pageTitleInput = document.getElementById('pageTitle');
const pageContentInput = document.getElementById('pageContent');
const pageImageInput = document.getElementById('pageImage');
const addPageBtn = document.getElementById('addPageBtn');
const downloadBtn = document.getElementById('downloadBtn');
const clearBtn = document.getElementById('clearBtn');
const bookPreview = document.getElementById('bookPreview');

// Event listeners
bookTitleInput.addEventListener('input', updateBookInfo);
bookAuthorInput.addEventListener('input', updateBookInfo);
addPageBtn.addEventListener('click', addPage);
downloadBtn.addEventListener('click', downloadBook);
clearBtn.addEventListener('click', clearAll);

// Update book info
function updateBookInfo() {
    bookData.title = bookTitleInput.value;
    bookData.author = bookAuthorInput.value;
    updatePreview();
}

// Add a new page
function addPage() {
    const pageTitle = pageTitleInput.value.trim();
    const pageContent = pageContentInput.value.trim();
    const pageImage = pageImageInput.value.trim();

    if (!pageTitle && !pageContent) {
        alert('Bitte füge mindestens einen Titel oder Inhalt hinzu!');
        return;
    }

    const page = {
        title: pageTitle || 'Unbenannte Seite',
        content: pageContent,
        image: pageImage
    };

    bookData.pages.push(page);
    
    // Clear inputs
    pageTitleInput.value = '';
    pageContentInput.value = '';
    pageImageInput.value = '';

    updatePreview();
}

// Update preview
function updatePreview() {
    if (bookData.pages.length === 0) {
        bookPreview.innerHTML = '<p class="empty-state">Füge Seiten hinzu, um eine Vorschau zu sehen...</p>';
        downloadBtn.disabled = true;
        return;
    }

    let html = '';
    
    if (bookData.title) {
        html += `<div class="page-item"><h4>📖 ${escapeHtml(bookData.title)}</h4>`;
        if (bookData.author) {
            html += `<p><em>von ${escapeHtml(bookData.author)}</em></p>`;
        }
        html += '</div>';
    }

    bookData.pages.forEach((page, index) => {
        html += `
            <div class="page-item">
                <span class="page-number">Seite ${index + 1}</span>
                <h4>${escapeHtml(page.title)}</h4>
                <p>${escapeHtml(page.content)}</p>
                ${page.image ? `<img src="${escapeHtml(page.image)}" alt="${escapeHtml(page.title)}" onerror="this.style.display='none'">` : ''}
            </div>
        `;
    });

    bookPreview.innerHTML = html;
    downloadBtn.disabled = false;
}

// Download book as HTML
function downloadBook() {
    const html = generateBookHTML();
    const blob = new Blob([html], { type: 'text/html' });
    const url = URL.createObjectURL(blob);
    
    const a = document.createElement('a');
    a.href = url;
    a.download = `${bookData.title || 'mein-buch'}.html`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);

    alert('Dein Buch wurde erfolgreich heruntergeladen! 📚');
}

// Generate complete HTML for the book
function generateBookHTML() {
    const title = bookData.title || 'Mein Interaktives Buch';
    const author = bookData.author || 'Unbekannter Autor';
    
    let pagesHTML = '';
    bookData.pages.forEach((page, index) => {
        pagesHTML += `
        <div class="page">
            <div class="page-number">Seite ${index + 1}</div>
            <h2>${escapeHtml(page.title)}</h2>
            <div class="content">${escapeHtml(page.content)}</div>
            ${page.image ? `<img src="${escapeHtml(page.image)}" alt="${escapeHtml(page.title)}">` : ''}
        </div>
        `;
    });

    return `<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${escapeHtml(title)}</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Georgia', serif;
            background: #f5f5dc;
            padding: 20px;
            line-height: 1.8;
        }
        
        .book-container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }
        
        .book-title {
            text-align: center;
            font-size: 2.5em;
            color: #333;
            margin-bottom: 10px;
            border-bottom: 3px solid #667eea;
            padding-bottom: 20px;
        }
        
        .book-author {
            text-align: center;
            font-style: italic;
            color: #666;
            margin-bottom: 40px;
            font-size: 1.2em;
        }
        
        .page {
            margin-bottom: 40px;
            padding: 30px;
            background: #fafafa;
            border-left: 5px solid #667eea;
            border-radius: 5px;
        }
        
        .page-number {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
            margin-bottom: 15px;
        }
        
        .page h2 {
            color: #333;
            margin-bottom: 15px;
            font-size: 1.8em;
        }
        
        .page .content {
            color: #444;
            white-space: pre-wrap;
            margin-bottom: 20px;
            font-size: 1.1em;
        }
        
        .page img {
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            margin-top: 15px;
        }
        
        @media print {
            body {
                background: white;
            }
            .book-container {
                box-shadow: none;
            }
            .page {
                page-break-inside: avoid;
            }
        }
    </style>
</head>
<body>
    <div class="book-container">
        <h1 class="book-title">${escapeHtml(title)}</h1>
        <div class="book-author">von ${escapeHtml(author)}</div>
        ${pagesHTML}
        <div style="text-align: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid #ddd; color: #999;">
            <small>Erstellt mit dem Interaktiven KI Book Builder</small>
        </div>
    </div>
</body>
</html>`;
}

// Clear all data
function clearAll() {
    if (bookData.pages.length === 0 && !bookData.title && !bookData.author) {
        return;
    }

    if (confirm('Möchtest du wirklich alles löschen?')) {
        bookData = {
            title: '',
            author: '',
            pages: []
        };
        
        bookTitleInput.value = '';
        bookAuthorInput.value = '';
        pageTitleInput.value = '';
        pageContentInput.value = '';
        pageImageInput.value = '';
        
        updatePreview();
    }
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Load saved data from localStorage on page load
window.addEventListener('load', () => {
    const saved = localStorage.getItem('bookData');
    if (saved) {
        try {
            const data = JSON.parse(saved);
            if (confirm('Möchtest du dein gespeichertes Buch laden?')) {
                bookData = data;
                bookTitleInput.value = bookData.title;
                bookAuthorInput.value = bookData.author;
                updatePreview();
            }
        } catch (e) {
            console.error('Error loading saved data:', e);
        }
    }
});

// Auto-save to localStorage
window.addEventListener('beforeunload', () => {
    if (bookData.pages.length > 0 || bookData.title || bookData.author) {
        localStorage.setItem('bookData', JSON.stringify(bookData));
    }
});
