#
# PySNMP MIB module CISCO-OTV-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-OTV-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:01 2026
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
ciscoOtvCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 622))
ciscoOtvCapability.setRevisions(('2013-07-29 00:00',))
if mibBuilder.loadTexts: ciscoOtvCapability.setLastUpdated('201307290000Z')
if mibBuilder.loadTexts: ciscoOtvCapability.setOrganization('Cisco Systems, Inc.')
ciscoOtvCapNxOSV06R0202PN7K = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 622, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOtvCapNxOSV06R0202PN7K = ciscoOtvCapNxOSV06R0202PN7K.setProductRelease('Cisco NX-OS 6.2(2) on Nexus 7000 series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOtvCapNxOSV06R0202PN7K = ciscoOtvCapNxOSV06R0202PN7K.setStatus('current')
mibBuilder.exportSymbols("CISCO-OTV-CAPABILITY", PYSNMP_MODULE_ID=ciscoOtvCapability, ciscoOtvCapNxOSV06R0202PN7K=ciscoOtvCapNxOSV06R0202PN7K, ciscoOtvCapability=ciscoOtvCapability)
