// Можно использовать для всплывающих уведомлений о бонусе
class SimpleModal {
    constructor(content) {
        this.content = content;
    }
    
    show() {
        const modal = document.createElement('div');
        modal.className = 'modal';
        modal.innerHTML = `
            <div class="modal-content">
                <span class="close">&times;</span>
                ${this.content}
            </div>
        `;
        document.body.appendChild(modal);
        
        modal.querySelector('.close').onclick = () => modal.remove();
    }
}

// Пример использования (можно подключить позже):
// const bonusModal = new SimpleModal('<p>Специальный бонус для вас!</p>');