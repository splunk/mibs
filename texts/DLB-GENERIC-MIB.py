#
# PySNMP MIB module DLB-GENERIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/deliberant/DLB-GENERIC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:05 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dlbMgmt, = mibBuilder.importSymbols("DELIBERANT-MIB", "dlbMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysLocation, = mibBuilder.importSymbols("SNMPv2-MIB", "sysLocation")
Integer32, MibIdentifier, Gauge32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, ModuleIdentity, TimeTicks, Counter32, ObjectIdentity, IpAddress, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "Gauge32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "ModuleIdentity", "TimeTicks", "Counter32", "ObjectIdentity", "IpAddress", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlbGenericMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 32761, 3, 1))
dlbGenericMIB.setRevisions(('2009-02-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlbGenericMIB.setRevisionsDescriptions(('First revision.',))
if mibBuilder.loadTexts: dlbGenericMIB.setLastUpdated('200902130000Z')
if mibBuilder.loadTexts: dlbGenericMIB.setOrganization('Deliberant')
if mibBuilder.loadTexts: dlbGenericMIB.setContactInfo('\n        Deliberant Customer Support\n        E-mail: support@deliberant.com')
if mibBuilder.loadTexts: dlbGenericMIB.setDescription('The Deliberant Generic MIB.')
dlbGenericMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1))
dlbGenericNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0))
dlbGenericInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 1))
dlbPowerLoss = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0, 1)).setObjects(("SNMPv2-MIB", "sysLocation"))
if mibBuilder.loadTexts: dlbPowerLoss.setStatus('current')
if mibBuilder.loadTexts: dlbPowerLoss.setDescription('This notification is sent on device boot after power loss or device crash.')
dlbAdministrativeReboot = NotificationType((1, 3, 6, 1, 4, 1, 32761, 3, 1, 1, 0, 2)).setObjects(("SNMPv2-MIB", "sysLocation"))
if mibBuilder.loadTexts: dlbAdministrativeReboot.setStatus('current')
if mibBuilder.loadTexts: dlbAdministrativeReboot.setDescription('This notification is sent on device boot after administrator rebooted device.')
mibBuilder.exportSymbols("DLB-GENERIC-MIB", dlbGenericNotifs=dlbGenericNotifs, dlbAdministrativeReboot=dlbAdministrativeReboot, dlbGenericMIBObjects=dlbGenericMIBObjects, dlbGenericInfo=dlbGenericInfo, dlbPowerLoss=dlbPowerLoss, PYSNMP_MODULE_ID=dlbGenericMIB, dlbGenericMIB=dlbGenericMIB)
