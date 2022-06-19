import { Component, OnInit } from '@angular/core';
import { faTwitter } from '@fortawesome/free-brands-svg-icons';
import { faInstagram } from '@fortawesome/free-brands-svg-icons';
import { faLinkedin } from '@fortawesome/free-brands-svg-icons';
import { faBars } from '@fortawesome/free-solid-svg-icons';
import { faXmark } from '@fortawesome/free-solid-svg-icons';
@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  faTwitter = faTwitter;
  faInstagram = faInstagram;
  faLinkedin = faLinkedin;
  faBars = faBars;
  faXmark = faXmark;

 
  faDefaultIcon = faBars

  constructor() { }

  ngOnInit(): void {
  }

  menuToggle(e: any): void{
    let list: any = document.querySelector('ul');
    this.faDefaultIcon === this.faBars ? (this.faDefaultIcon = this.faXmark, list.classList.add('opacity-100')) :( this.faDefaultIcon = this.faBars ,list.classList.remove('opacity-100'))
  }

}
