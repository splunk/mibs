#
# PySNMP MIB module CISCO-L4L7MODULE-RESOURCE-LIMIT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-L4L7MODULE-RESOURCE-LIMIT-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:57 2026
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
ciscoL4L7ModRsrcLimCap = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 499))
ciscoL4L7ModRsrcLimCap.setRevisions(('2008-07-22 00:00', '2008-07-21 00:00', '2006-04-19 00:00',))
if mibBuilder.loadTexts: ciscoL4L7ModRsrcLimCap.setLastUpdated('200807220000Z')
if mibBuilder.loadTexts: ciscoL4L7ModRsrcLimCap.setOrganization('Cisco Systems, Inc.')
cL4L7ModRsrcLimCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 499, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapACSWV03R000 = cL4L7ModRsrcLimCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapACSWV03R000 = cL4L7ModRsrcLimCapACSWV03R000.setStatus('current')
cL4L7ModRsrcLimCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 499, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA1R700 = cL4L7ModRsrcLimCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                for ACE 4710 Application Control Engine \n                Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA1R700 = cL4L7ModRsrcLimCapc4710aceVA1R700.setStatus('current')
cL4L7ModRsrcLimCapc4710aceVA3R10 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 499, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA3R10 = cL4L7ModRsrcLimCapc4710aceVA3R10.setProductRelease('ACSW (Application Control Software) A3(1.0)\n                    for ACE 4710 Application Control Engine \n                    Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cL4L7ModRsrcLimCapc4710aceVA3R10 = cL4L7ModRsrcLimCapc4710aceVA3R10.setStatus('current')
mibBuilder.exportSymbols("CISCO-L4L7MODULE-RESOURCE-LIMIT-CAPABILITY", cL4L7ModRsrcLimCapACSWV03R000=cL4L7ModRsrcLimCapACSWV03R000, PYSNMP_MODULE_ID=ciscoL4L7ModRsrcLimCap, cL4L7ModRsrcLimCapc4710aceVA3R10=cL4L7ModRsrcLimCapc4710aceVA3R10, cL4L7ModRsrcLimCapc4710aceVA1R700=cL4L7ModRsrcLimCapc4710aceVA1R700, ciscoL4L7ModRsrcLimCap=ciscoL4L7ModRsrcLimCap)
