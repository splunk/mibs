#
# PySNMP MIB module CISCO-IEEE8021-CFM-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IEEE8021-CFM-EXT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIeee8021CfmExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 576))
ciscoIeee8021CfmExtCapability.setRevisions(('2008-12-05 00:00',))
if mibBuilder.loadTexts: ciscoIeee8021CfmExtCapability.setLastUpdated('200812050000Z')
if mibBuilder.loadTexts: ciscoIeee8021CfmExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoIeee8021CfmExtCapCatOSV08R0702 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 576, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmExtCapCatOSV08R0702 = ciscoIeee8021CfmExtCapCatOSV08R0702.setProductRelease('Cisco CatOS 8.7(2).')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIeee8021CfmExtCapCatOSV08R0702 = ciscoIeee8021CfmExtCapCatOSV08R0702.setStatus('current')
mibBuilder.exportSymbols("CISCO-IEEE8021-CFM-EXT-CAPABILITY", ciscoIeee8021CfmExtCapability=ciscoIeee8021CfmExtCapability, ciscoIeee8021CfmExtCapCatOSV08R0702=ciscoIeee8021CfmExtCapCatOSV08R0702, PYSNMP_MODULE_ID=ciscoIeee8021CfmExtCapability)
