[toc]


# 《正点原子FreeRTOS手把手教学》

**S6**

任务优先级：数字越大，优先级越高

任务堆栈大小=值*4

**S7**

- xTaskCreate：使用动态方法创建一个任务
- xTaskCreateStatic():使用静态的方创建一个任务
- xTaskCreateRestricted():创建一个使用MPU进行限制的任务，相关内存使用动态内存分配
- vTaskDelete()：删除一个任务

**S9**

- vTaskSuspend():挂起一个任务
- vTaskResume():恢复一个任务的运行
- xTaskResumeFromISR():中断服务函数中恢复一个任务的运行

**S10**

