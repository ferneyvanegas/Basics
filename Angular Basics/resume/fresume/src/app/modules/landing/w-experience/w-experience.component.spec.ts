import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WExperienceComponent } from './w-experience.component';

describe('WExperienceComponent', () => {
  let component: WExperienceComponent;
  let fixture: ComponentFixture<WExperienceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WExperienceComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WExperienceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
