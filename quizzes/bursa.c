#include <stdio.h>

void Bursa(int arr[], int size, int* buy_idx, int* sell_idx, int* stock_profit)
{
	int i;
	int buy[2] = {0};
	int sell[2] = {0};
	int profit[3] = {0};
	
	buy[1] =  arr[0];
	sell[1] = arr[0];
	
	
	for(i = 1; i < size; i++)
	{
		if(sell[1] < arr[i])
		{
			sell[0] = i;
			sell[1] = arr[i];
			if(profit[2] < sell[1] - buy[1])
			{
				profit[0] = buy[0];
				profit[1] = sell[0];
				profit[2] = arr[sell[0]] - arr[buy[0]];
			}
		}
		if(buy[1] > arr[i])
		{
			sell[0] = i;
			sell[1] = arr[i];
			buy[0] = i;
			buy[1] = arr[i];
		}
	}
	
	*buy_idx = profit[0];
	*sell_idx = profit[1];
	*stock_profit = profit[2];
	
	printf("You should buy at index %d, and sell at index %d.\nThe profit is %d.\n", profit[0], profit[1], profit[2]);
}

int main()
{
	int profit[] = {0};
	int arr[] = {6, 1, 3, 5, 1, 4, 4, 2};
	int size = sizeof(arr) / sizeof(int);
	
	StockProfit(arr, size, &profit[0], &profit[1], &profit[2]);
	
	return 0;
}
