#
# PySNMP MIB module CISCO-SLB-HEALTH-MON-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-SLB-HEALTH-MON-CAPABILITY
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
ciscoSlbHealthMonCapapbility = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 508))
ciscoSlbHealthMonCapapbility.setRevisions(('2008-07-03 00:00', '2008-02-08 00:00', '2006-06-02 00:00',))
if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setLastUpdated('200807030000Z')
if mibBuilder.loadTexts: ciscoSlbHealthMonCapapbility.setOrganization('Cisco Systems, Inc.')
ciscoSlbHealthMonCapabilityACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 508, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapabilityACSWV03R000 = ciscoSlbHealthMonCapabilityACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapabilityACSWV03R000 = ciscoSlbHealthMonCapabilityACSWV03R000.setStatus('current')
ciscoSlbHealthMonCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 508, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA1R700 = ciscoSlbHealthMonCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                for ACE 4710 Application Control Engine \n                Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA1R700 = ciscoSlbHealthMonCapc4710aceVA1R700.setStatus('current')
ciscoSlbHealthMonCapc4710aceVA3R100 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 508, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA3R100 = ciscoSlbHealthMonCapc4710aceVA3R100.setProductRelease('ACSW (Application Control Software) A3(1.0)\n                for ACE 4710 Application Control Engine \n                Appliance')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSlbHealthMonCapc4710aceVA3R100 = ciscoSlbHealthMonCapc4710aceVA3R100.setStatus('current')
mibBuilder.exportSymbols("CISCO-SLB-HEALTH-MON-CAPABILITY", PYSNMP_MODULE_ID=ciscoSlbHealthMonCapapbility, ciscoSlbHealthMonCapapbility=ciscoSlbHealthMonCapapbility, ciscoSlbHealthMonCapc4710aceVA1R700=ciscoSlbHealthMonCapc4710aceVA1R700, ciscoSlbHealthMonCapc4710aceVA3R100=ciscoSlbHealthMonCapc4710aceVA3R100, ciscoSlbHealthMonCapabilityACSWV03R000=ciscoSlbHealthMonCapabilityACSWV03R000)
