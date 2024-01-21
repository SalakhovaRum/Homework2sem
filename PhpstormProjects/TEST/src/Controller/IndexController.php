<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class IndexController extends AbstractController
{
    #[Route('/', name: 'app_index')]
    public function index(): Response
    {
        return $this->render('index/index.html.twig', [
            'controller_name' => 'IndexController',
        ]);
    }

    #[Route('/shop/list', name: 'app_shopList')]
    public function shopList(): Response
    {
        return $this->render('index/index.html.twig', [
            'controller_name' => 'SHOP LIST',
        ]);
    }

    #[Route('/shop/item/{id<\d+>}', name: 'app_shopItem')]
    public function shopItem(int $id): Response
    {
        return $this->render('index/index.html.twig', [
            'controller_name' => 'SHOP ITEM' . $id,
        ]);
    }
}
