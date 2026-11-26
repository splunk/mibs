#
# PySNMP MIB module CISCO-GPRS-GTP-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GPRS-GTP-CAPABILITY
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
cgprsGtpCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 212))
cgprsGtpCapability.setRevisions(('2001-12-20 16:00', '2001-06-05 16:00',))
if mibBuilder.loadTexts: cgprsGtpCapability.setLastUpdated('200112201600Z')
if mibBuilder.loadTexts: cgprsGtpCapability.setOrganization('Cisco Systems, Inc.')
cgprsGtpCapabilityV12R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 212, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R01 = cgprsGtpCapabilityV12R01.setProductRelease('Cisco IOS 12.1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R01 = cgprsGtpCapabilityV12R01.setStatus('current')
cgprsGtpCapabilityV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 212, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R02 = cgprsGtpCapabilityV12R02.setProductRelease('Cisco IOS 12.2(7)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsGtpCapabilityV12R02 = cgprsGtpCapabilityV12R02.setStatus('current')
mibBuilder.exportSymbols("CISCO-GPRS-GTP-CAPABILITY", cgprsGtpCapability=cgprsGtpCapability, PYSNMP_MODULE_ID=cgprsGtpCapability, cgprsGtpCapabilityV12R01=cgprsGtpCapabilityV12R01, cgprsGtpCapabilityV12R02=cgprsGtpCapabilityV12R02)
