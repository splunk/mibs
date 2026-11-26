#
# PySNMP MIB module CISCO-SWITCH-RATE-LIMITER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SWITCH-RATE-LIMITER-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSwitchRateLimiterCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 606))
ciscoSwitchRateLimiterCapability.setRevisions(('2011-07-27 00:00',))
if mibBuilder.loadTexts: ciscoSwitchRateLimiterCapability.setLastUpdated('201107270000Z')
if mibBuilder.loadTexts: ciscoSwitchRateLimiterCapability.setOrganization('Cisco Systems, Inc.')
ciscoRateLimiterCapNxOSV05R0201PN7k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 606, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRateLimiterCapNxOSV05R0201PN7k = ciscoRateLimiterCapNxOSV05R0201PN7k.setProductRelease('Cisco NX-OS 5.2(1) on Nexus 7000\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRateLimiterCapNxOSV05R0201PN7k = ciscoRateLimiterCapNxOSV05R0201PN7k.setStatus('current')
mibBuilder.exportSymbols("CISCO-SWITCH-RATE-LIMITER-CAPABILITY", ciscoRateLimiterCapNxOSV05R0201PN7k=ciscoRateLimiterCapNxOSV05R0201PN7k, PYSNMP_MODULE_ID=ciscoSwitchRateLimiterCapability, ciscoSwitchRateLimiterCapability=ciscoSwitchRateLimiterCapability)
