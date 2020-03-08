"""
Configuration file for the PL_Stat app.
Author: Maciej Cisowski
"""
from datetime import datetime
from io import StringIO


logger_root_config = {'version': 1,
                      'disable_existing_loggers': False,
                      'loggers':
                          {
                              '':
                                  {
                                      'level': 'DEBUG',
                                      'handlers': ['file_handler', 'string_handler', 'terminal']
                                  },
                              'helpers_logger':
                                  {
                                      'level': 'DEBUG',
                                      'handlers': ['file_handler', 'string_handler', 'terminal']
                                  }
                          },
                      'formatters':
                          {
                              'default':
                                  {
                                      'format': '%(asctime)s : %(name)s : %(funcName)s : %(lineno)d '
                                                ': %(levelname)s : %(message)s'
                                  }
                          },
                      'handlers':
                          {
                              'file_handler':
                                  {
                                      'class': 'logging.FileHandler',
                                      'filename': './logs/runtimeLog' + str(datetime.utcnow()),
                                      'formatter': 'default'
                                  },
                              'string_handler':
                                  {
                                      'class': 'logging.StreamHandler',
                                      'stream': StringIO(),
                                      'formatter': 'default'
                                  },
                              'terminal':
                                  {
                                      'class': 'logging.StreamHandler',
                                      'formatter': 'default'
                                  }
                          }
                      }

