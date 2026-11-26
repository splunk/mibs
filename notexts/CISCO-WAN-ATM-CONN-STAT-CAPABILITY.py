#
# PySNMP MIB module CISCO-WAN-ATM-CONN-STAT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WAN-ATM-CONN-STAT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
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
ciscoWanAtmConnStatCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 9999))
ciscoWanAtmConnStatCapability.setRevisions(('2003-04-08 00:00', '2001-03-21 00:00',))
if mibBuilder.loadTexts: ciscoWanAtmConnStatCapability.setLastUpdated('200304080000Z')
if mibBuilder.loadTexts: ciscoWanAtmConnStatCapability.setOrganization('Cisco Systems, Inc.')
cwaConnStatCapabilityAxsmV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwaConnStatCapabilityAxsmV21R60 = cwaConnStatCapabilityAxsmV21R60.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwaConnStatCapabilityAxsmV21R60 = cwaConnStatCapabilityAxsmV21R60.setStatus('current')
cwAtmConnStatCapabilityAxsmeV2R0170 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityAxsmeV2R0170 = cwAtmConnStatCapabilityAxsmeV2R0170.setProductRelease('MGX8850 Release 2.1.70')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityAxsmeV2R0170 = cwAtmConnStatCapabilityAxsmeV2R0170.setStatus('current')
cwAtmConnStatCapabilityPxm1eV2R300 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityPxm1eV2R300 = cwAtmConnStatCapabilityPxm1eV2R300.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwAtmConnStatCapabilityPxm1eV2R300 = cwAtmConnStatCapabilityPxm1eV2R300.setStatus('current')
cwacsCapabilityAxsmxgV4R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 9999, 4))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwacsCapabilityAxsmxgV4R00 = cwacsCapabilityAxsmxgV4R00.setProductRelease('MGX8950 Release 4.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cwacsCapabilityAxsmxgV4R00 = cwacsCapabilityAxsmxgV4R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-ATM-CONN-STAT-CAPABILITY", cwAtmConnStatCapabilityPxm1eV2R300=cwAtmConnStatCapabilityPxm1eV2R300, cwacsCapabilityAxsmxgV4R00=cwacsCapabilityAxsmxgV4R00, cwaConnStatCapabilityAxsmV21R60=cwaConnStatCapabilityAxsmV21R60, cwAtmConnStatCapabilityAxsmeV2R0170=cwAtmConnStatCapabilityAxsmeV2R0170, PYSNMP_MODULE_ID=ciscoWanAtmConnStatCapability, ciscoWanAtmConnStatCapability=ciscoWanAtmConnStatCapability)
